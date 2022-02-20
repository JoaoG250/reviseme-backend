# Generated by Django 3.2.9 on 2022-02-20 15:14

import core.utils.models
from django.db import migrations, models
import django.db.models.deletion
import topic.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("subject", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Topic",
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
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Creation date"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Last modified date"
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField(max_length=250)),
                (
                    "image",
                    models.ImageField(
                        null=True, upload_to=core.utils.models.file_upload_path
                    ),
                ),
                ("active", models.BooleanField(default=True)),
                (
                    "subject",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="topics",
                        to="subject.subject",
                    ),
                ),
            ],
            options={
                "unique_together": {("subject", "name")},
            },
        ),
        migrations.CreateModel(
            name="TopicLink",
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
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Creation date"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Last modified date"
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("url", models.URLField()),
                (
                    "topic",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="links",
                        to="topic.topic",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="TopicFile",
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
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Creation date"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Last modified date"
                    ),
                ),
                (
                    "file",
                    models.FileField(upload_to=core.utils.models.file_upload_path),
                ),
                (
                    "file_type",
                    models.CharField(
                        choices=[
                            ("PDF", "PDF"),
                            ("IMAGE", "Image"),
                            ("VIDEO", "Video"),
                            ("AUDIO", "Audio"),
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "topic",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="files",
                        to="topic.topic",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="TopicRevision",
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
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Creation date"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Last modified date"
                    ),
                ),
                (
                    "phase",
                    models.CharField(
                        choices=[
                            ("1D", "1 Day"),
                            ("7D", "7 Days"),
                            ("30D", "30 Days"),
                            ("90D", "90 Days"),
                        ],
                        default="1D",
                        max_length=10,
                    ),
                ),
                (
                    "revision_date",
                    models.DateField(default=topic.models.revision_date_default_value),
                ),
                ("complete", models.BooleanField(default=False)),
                (
                    "topic",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="revisions",
                        to="topic.topic",
                    ),
                ),
            ],
            options={
                "unique_together": {("topic", "phase")},
            },
        ),
    ]
