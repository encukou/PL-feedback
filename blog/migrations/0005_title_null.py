# Generated by Django 2.1.7 on 2019-02-27 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_longer_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
