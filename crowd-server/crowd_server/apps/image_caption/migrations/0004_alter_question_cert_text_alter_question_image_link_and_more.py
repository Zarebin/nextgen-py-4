# Generated by Django 4.1 on 2022-09-09 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("image_caption", "0003_alter_question_not_sure_count"),
    ]

    operations = [
        migrations.AlterField(
            model_name="question",
            name="cert_text",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="question",
            name="image_link",
            field=models.CharField(max_length=800),
        ),
        migrations.AlterField(
            model_name="question",
            name="question_text",
            field=models.CharField(max_length=100),
        ),
    ]
