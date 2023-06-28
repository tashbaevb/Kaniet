# Generated by Django 4.1.3 on 2023-02-09 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_home_about_delete_home"),
    ]

    operations = [
        migrations.CreateModel(
            name="Do",
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
                ("title", models.CharField(max_length=200)),
                ("text", models.TextField(max_length=2000)),
                ("img", models.ImageField(upload_to="")),
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
                ("title", models.CharField(max_length=200)),
                ("text", models.TextField(max_length=5000)),
            ],
        ),
        migrations.RenameField(
            model_name="home_about",
            old_name="description",
            new_name="text",
        ),
    ]