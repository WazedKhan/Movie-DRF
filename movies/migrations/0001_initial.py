# Generated by Django 4.1.7 on 2023-03-19 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Movie",
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
                ("title", models.CharField(max_length=128)),
                ("description", models.TextField(max_length=2048)),
                ("release_date", models.DateField()),
                ("rating", models.PositiveSmallIntegerField()),
                ("us_gross", models.IntegerField(default=0)),
                ("worldwide_gross", models.IntegerField(default=0)),
            ],
        ),
    ]
