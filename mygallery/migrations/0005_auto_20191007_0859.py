# Generated by Django 2.2.6 on 2019-10-07 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mygallery', '0004_auto_20191005_1000'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imagepost',
            options={'ordering': ['-created_on']},
        ),
    ]
