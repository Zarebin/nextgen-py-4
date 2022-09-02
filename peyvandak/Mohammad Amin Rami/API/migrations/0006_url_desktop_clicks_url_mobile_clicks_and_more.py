# Generated by Django 4.1 on 2022-08-31 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0005_url_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='desktop_clicks',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='url',
            name='mobile_clicks',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='url',
            name='clicks',
            field=models.IntegerField(blank=True),
        ),
    ]
