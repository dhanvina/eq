# Generated by Django 4.1.4 on 2023-09-20 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lab", "0005_alter_labinchargelogin_email_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="labinchargelogin",
            name="password",
            field=models.CharField(max_length=20),
        ),
    ]
