# Generated by Django 5.1.2 on 2024-11-05 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0002_alter_project_user"),
    ]

    operations = [
        migrations.RenameField(
            model_name="project", old_name="create_at", new_name="created_at",
        ),
        migrations.RenameField(
            model_name="project", old_name="update_at", new_name="updated_at",
        ),
    ]
