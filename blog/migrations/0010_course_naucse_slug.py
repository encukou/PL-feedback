# Generated by Django 2.2.10 on 2020-05-01 13:29

import blog.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20191219_1401'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='naucse_slug',
            field=blog.models.NaucseSlugField(help_text='Pokud je vyplněno, kurz bude propojen s daným kurzem na naucse.', max_length=500, null=True),
        ),
    ]
