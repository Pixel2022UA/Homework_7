# Generated by Django 4.2 on 2023-04-30 13:12

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("teachers", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="studentsgroup",
            name="group",
        ),
        migrations.RemoveField(
            model_name="studentsgroup",
            name="student",
        ),
        migrations.DeleteModel(
            name="Group",
        ),
        migrations.DeleteModel(
            name="Student",
        ),
        migrations.DeleteModel(
            name="StudentsGroup",
        ),
    ]