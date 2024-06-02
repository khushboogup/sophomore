# Generated by Django 5.0.6 on 2024-06-01 21:06

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("personalblog", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="categories",
        ),
        migrations.RemoveField(
            model_name="comment",
            name="post",
        ),
        migrations.DeleteModel(
            name="Category",
        ),
        migrations.DeleteModel(
            name="Comment",
        ),
        migrations.DeleteModel(
            name="Post",
        ),
    ]