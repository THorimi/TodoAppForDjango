# Generated by Django 5.0.4 on 2024-04-23 07:08

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_alter_todomodel_duedate_alter_todomodel_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todomodel',
            name='duedate',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='期日'),
        ),
    ]