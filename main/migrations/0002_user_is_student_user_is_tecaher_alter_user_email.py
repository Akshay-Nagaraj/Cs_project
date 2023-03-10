# Generated by Django 4.1.5 on 2023-01-15 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="is_student",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="user",
            name="is_tecaher",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(
                blank=True, max_length=254, verbose_name="email address"
            ),
        ),
    ]
