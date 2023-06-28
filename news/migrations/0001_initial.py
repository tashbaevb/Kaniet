# Generated by Django 4.1.3 on 2023-02-09 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                ("number", models.CharField(max_length=100)),
                ("address", models.TextField(max_length=200)),
                ("instagram", models.TextField(max_length=200)),
                ("facebook", models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="New",
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
                ("img", models.ImageField(upload_to="")),
                ("title", models.TextField(max_length=400)),
                ("text", models.TextField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name="Service",
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
                ("img", models.ImageField(upload_to="")),
                ("title", models.CharField(max_length=200)),
                ("text", models.TextField(max_length=4000)),
            ],
        ),
    ]
