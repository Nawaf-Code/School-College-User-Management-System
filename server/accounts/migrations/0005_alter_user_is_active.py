# Generated by Django 4.2.4 on 2023-08-26 16:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0004_user_code"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="is_active",
            field=models.BooleanField(default=False),
        ),
    ]