# Generated by Django 3.2.9 on 2022-01-15 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='type',
            old_name='describr',
            new_name='describe',
        ),
    ]
