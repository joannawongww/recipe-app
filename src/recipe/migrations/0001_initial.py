# Generated by Django 4.2.7 on 2023-11-29 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('cooking_time', models.PositiveIntegerField(help_text='in mins')),
                ('ingredients', models.CharField(help_text='separate ingredient by a comma & a space', max_length=255)),
                ('description', models.TextField()),
            ],
        ),
    ]
