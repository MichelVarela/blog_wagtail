# Generated by Django 4.1.8 on 2023-04-22 15:17

from django.db import migrations
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('registration02', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration02',
            name='cta_name',
            field=wagtail.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='registration02',
            name='logos',
            field=wagtail.fields.StreamField([('image', wagtail.images.blocks.ImageChooserBlock(required=True, template='base/blocks/image_block.html'))], use_json_field=None),
        ),
    ]
