# Generated by Django 4.0.4 on 2022-04-26 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ukstagram', '0003_post_is_public'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='ip',
            field=models.GenericIPAddressField(null=True),
        ),
    ]
