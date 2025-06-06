# Generated by Django 5.2 on 2025-04-23 16:29

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Address",
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
                ("label", models.CharField(max_length=255)),
                ("housenumber", models.CharField(max_length=20)),
                ("street", models.CharField(max_length=255)),
                ("postcode", models.CharField(max_length=10)),
                ("citycode", models.CharField(max_length=10)),
                ("latitude", models.FloatField()),
                ("longitude", models.FloatField()),
            ],
        ),
    ]
