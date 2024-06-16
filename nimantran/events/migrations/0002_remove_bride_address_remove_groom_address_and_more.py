# Generated by Django 5.0.6 on 2024-06-16 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bride',
            name='address',
        ),
        migrations.RemoveField(
            model_name='groom',
            name='address',
        ),
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]