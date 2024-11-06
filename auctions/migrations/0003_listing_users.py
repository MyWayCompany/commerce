# Generated by Django 5.1.3 on 2024-11-06 14:37

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_category_comment_listing'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='users',
            field=models.ManyToManyField(related_name='watch_listing', to=settings.AUTH_USER_MODEL),
        ),
    ]
