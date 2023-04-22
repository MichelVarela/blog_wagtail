from wagtail.blocks import (
    RichTextBlock,
    StreamBlock,
)

from wagtail.images.blocks import ImageChooserBlock

class ThankYouSection(StreamBlock):
    title = RichTextBlock(features=['h1', 'h2', 'h3', 'bold', 'italic', 'link'], icon='title', required=False)
    text = RichTextBlock(features=['bold', 'italic', 'link', 'ol', 'ul'], required=False)
    ics = RichTextBlock(features=['bold', 'italic', 'link'], icon='link', required=False)

class ImageBlock(StreamBlock):
    image = ImageChooserBlock(template='base/blocks/image_block.html', required=True)

class HeroSection(StreamBlock):
    title = RichTextBlock(features=['h1', 'h2', 'h3', 'bold', 'italic', 'link'], icon='title')
    text = RichTextBlock(features=['bold', 'italic', 'link', 'ol', 'ul'])
    date = RichTextBlock(features=['bold', 'italic'], required=False)
    hour = RichTextBlock(features=['bold', 'italic'], required=False)
    location = RichTextBlock(features=['bold', 'italic', 'link'], icon='link', required=False)
    hero_image = ImageChooserBlock(template='base/blocks/image_block.html', required=True)

class BaseStreamBlock(StreamBlock):
    title = RichTextBlock(features=['h1', 'h2', 'h3', 'bold', 'italic', 'link'], icon='title')
    image_block = ImageChooserBlock(template='base/blocks/image_block.html', required=True)
    text = RichTextBlock(features=['bold', 'italic', 'link', 'ol', 'ul'])
    # permite embeber archivos de video en nuestras views utilizando la URI del mismo