# Generated by Django 4.1.4 on 2023-09-20 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lab", "0003_labinchargeregister"),
    ]

    operations = [
        migrations.CreateModel(
            name="LabInchargeLogin",
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
                ("email", models.EmailField(max_length=254, unique=True)),
                ("password", models.CharField(max_length=20)),
            ],
        ),
    ]
