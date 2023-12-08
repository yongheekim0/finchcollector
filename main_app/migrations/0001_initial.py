# Generated by Django 5.0 on 2023-12-08 08:46

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Finch",
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
                ("name", models.CharField(max_length=100)),
                ("habitat", models.CharField(max_length=100)),
                ("description", models.TextField(max_length=300)),
                ("diet", models.CharField(max_length=100)),
            ],
        ),
    ]
