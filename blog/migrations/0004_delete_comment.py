# Generated by Django 3.2.5 on 2024-09-06 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20240906_1024'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]