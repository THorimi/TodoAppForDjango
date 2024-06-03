# Generated by Django 5.0.4 on 2024-04-17 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('memo', models.TextField()),
                ('priority', models.CharField(choices=[('danger', 'high'), ('warning', 'normal'), ('primary', 'low')], max_length=50, null=True)),
                ('duedate', models.DateField()),
                ('complete', models.BooleanField(default=False)),
            ],
        ),
    ]
