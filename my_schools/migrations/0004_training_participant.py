# Generated by Django 2.1.7 on 2019-05-19 17:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('my_schools', '0003_auto_20190506_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='training',
            name='participant',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
