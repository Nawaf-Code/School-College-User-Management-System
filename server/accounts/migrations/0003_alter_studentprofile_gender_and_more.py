# Generated by Django 4.2.4 on 2023-08-14 21:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0002_student_supervisor_studentprofile"),
    ]

    operations = [
        migrations.AlterField(
            model_name="studentprofile",
            name="Gender",
            field=models.CharField(
                choices=[("MALE", "Male"), ("FEMALE", "Female")], default="none"
            ),
        ),
        migrations.AlterField(
            model_name="studentprofile",
            name="Is_Leader",
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name="studentprofile",
            name="Major",
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name="studentprofile",
            name="Status",
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.CreateModel(
            name="SupervisorProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Status", models.BooleanField(blank=True, default=False, null=True)),
                ("Major", models.CharField(blank=True, max_length=2, null=True)),
                (
                    "Supervisor_For",
                    models.CharField(
                        choices=[
                            ("MALE", "Male"),
                            ("FEMALE", "Female"),
                            ("MALE_FEMALE", "Male_Female"),
                        ],
                        default="none",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
