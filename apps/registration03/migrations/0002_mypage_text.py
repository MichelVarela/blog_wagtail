# Generated by Django 4.1.8 on 2023-04-22 23:17

from django.db import migrations
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('registration03', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mypage',
            name='text',
            field=wagtail.fields.RichTextField(blank=True),
        ),
    ]
