# Generated by Django 4.1.8 on 2023-04-21 18:13

from django.db import migrations
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('registration01', '0002_alter_registration01_thank_you_section'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration01',
            name='cta_name',
            field=wagtail.fields.RichTextField(default='Enviar'),
            preserve_default=False,
        ),
    ]
