from django.db import models
from wagtail.models import Page
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import (
    FieldPanel, FieldRowPanel,
    InlinePanel, MultiFieldPanel
)
from wagtail.fields import RichTextField, StreamField
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField

from apps.base import blocks

class ArcservePage(Page):
    template = 'registration02/arcserve_page.html'
    description = models.CharField(max_length=255, blank=True,)
    content_panels = Page.content_panels + [FieldPanel("description", classname="full")]

    subpage_types = ['Registration02']


class FormField(AbstractFormField):
    page = ParentalKey('Registration02', on_delete=models.CASCADE, related_name='form_fields')


class Registration02(AbstractEmailForm):
    template = 'registration02/registration02_page.html'

    logos = StreamField(
        blocks.ImageBlock()
    )

    hero_section = StreamField(
        blocks.HeroSection()
    )

    cta_name = RichTextField(features=['bold', 'italic'], blank=True)
    
    thank_you_section = StreamField(
        blocks.ThankYouSection(),
        blank=True,
    )

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('logos'),
        FieldPanel('hero_section'),
        MultiFieldPanel([
            InlinePanel('form_fields', label="Fields"),
            FieldPanel('cta_name'),
        ], 'Form'),
        FieldPanel('thank_you_section'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
    ]

    parent_page_types = ['ArcservePage']