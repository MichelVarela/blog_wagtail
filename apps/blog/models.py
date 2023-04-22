from django.db import models

from wagtail.models import Page
from wagtail.core import hooks
from wagtail.fields import StreamField
# FieldPanel permite editar 
from wagtail.admin.edit_handlers import (
    FieldPanel,
)

from apps.base.blocks import BaseStreamBlock

from wagtail.contrib.routable_page.models import RoutablePageMixin, route


class BlogPage(RoutablePageMixin, Page):
    description = models.CharField(max_length=255, blank=True,)

    content_panels = Page.content_panels + [FieldPanel("description", classname="full")]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['blog_page'] = self
        context['posts'] = self.posts
        return context

    def get_posts(self):
        return PostPage.objects.descendant_of(self).live()

    @route(r'^tag/(?P<tag>[-\w]+)/$')
    def post_by_tag(self, request, tag, *args, **kwargs):
        self.posts = self.get_posts().filter(tags__slug=tag)
        return self.render(request)

    @route(r'^category/(?P<category>[-\w]+)/$')
    def post_by_category(self, request, category, *args, **kwargs):
        self.posts = self.get_posts().filter(categories__blog_category__slug=category)
        return self.render(request)

    @route(r'^$')
    def post_list(self, request, *args, **kwargs):
        self.posts = self.get_posts()
        return self.render(request)
    
@hooks.register('register_page_types')
def register_my_page():
    return [BlogPage]


class PostPage(Page):
    date = models.DateField('Post date')
    summary = models.CharField(max_length=250)
    # los streamField requieren una serie de blocks generados en base/blocks.py
    body = StreamField(
        BaseStreamBlock(),
        blank=True
    )

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('summary'),
        FieldPanel('body')
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['blog_page'] = self.get_parent().specific
        return context

    # "parent_page_types", indicamos que esta page va a estar disponible solo para el padre indicado en la list
    parent_page_types = ['BlogPage']