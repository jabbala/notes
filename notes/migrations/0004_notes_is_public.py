# Generated by Django 5.1.7 on 2025-03-15 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("notes", "0003_notes_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="notes",
            name="is_public",
            field=models.BooleanField(default=True),
        ),
    ]
