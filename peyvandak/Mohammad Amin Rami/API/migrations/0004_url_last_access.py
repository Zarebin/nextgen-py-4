# Generated by Django 4.1 on 2022-08-24 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0003_alter_url_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='last_access',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
