# Generated by Django 4.1.5 on 2023-05-11 09:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Exams",
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
                ("exam_name", models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name="Grade_and_Section",
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
                ("Grade", models.PositiveSmallIntegerField()),
                ("Section", models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name="Teacher",
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
                ("subjects", models.CharField(max_length=254, null=True)),
                ("is_classTeacher", models.BooleanField(default=False)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Subjects",
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
                ("subject", models.CharField(max_length=254)),
                ("is_core", models.BooleanField()),
                ("is_elective", models.BooleanField()),
                (
                    "course",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.grade_and_section",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Student",
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
                ("first_name", models.CharField(max_length=254)),
                ("last_name", models.CharField(max_length=254)),
                ("DOB", models.DateField(max_length=254)),
                ("roll_no", models.PositiveSmallIntegerField(default=None)),
                ("subject_list", models.CharField(max_length=254, null=True)),
                (
                    "grade_and_section",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.grade_and_section",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Marks",
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
                ("assigned_marks", models.IntegerField(null=True)),
                (
                    "exam",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main.exams"
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main.student"
                    ),
                ),
                (
                    "subject",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main.subjects"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="grade_and_section",
            name="class_teacher",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="main.teacher"
            ),
        ),
        migrations.CreateModel(
            name="Attendance",
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
                ("date", models.DateField()),
                ("morning", models.BooleanField(default=True, null=True)),
                ("afternoon", models.BooleanField(default=True, null=True)),
                (
                    "grade_and_section",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.grade_and_section",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main.student"
                    ),
                ),
            ],
        ),
        migrations.AddConstraint(
            model_name="student",
            constraint=models.UniqueConstraint(
                fields=("grade_and_section", "roll_no"), name="Unique Roll"
            ),
        ),
        migrations.AddConstraint(
            model_name="marks",
            constraint=models.UniqueConstraint(
                fields=("exam", "subject", "student"), name="Unique marks entry"
            ),
        ),
        migrations.AddConstraint(
            model_name="attendance",
            constraint=models.UniqueConstraint(
                fields=("student", "date"), name="Unique attendance"
            ),
        ),
    ]
