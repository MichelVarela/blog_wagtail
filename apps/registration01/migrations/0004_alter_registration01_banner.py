# Generated by Django 4.1.8 on 2023-04-22 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
        ('registration01', '0003_registration01_cta_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration01',
            name='banner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.image'),
        ),
    ]
