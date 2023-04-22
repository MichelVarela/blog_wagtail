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

class GooglePage(Page):
    description = models.CharField(max_length=255, blank=True,)
    content_panels = Page.content_panels + [FieldPanel("description", classname="full")]

    subpage_types = ['Registration01']


class FormField(AbstractFormField):
    page = ParentalKey('Registration01', on_delete=models.CASCADE, related_name='form_fields')


class Registration01(AbstractEmailForm):
    template = 'registration01/registration01_page.html'

    banner = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        null=True
    )

    cta_name = RichTextField(features=['bold', 'italic'])

    text = RichTextField(features=['bold', 'italic', 'link', 'ol', 'ul'], blank=True)
    
    thank_you_section = StreamField(
        blocks.ThankYouSection(),
        blank=True
    )

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('banner'),
        InlinePanel('form_fields', label="Form fields"),
        FieldPanel('cta_name'),
        FieldPanel('text'),
        FieldPanel('thank_you_section'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
    ]

    parent_page_types = ['GooglePage']