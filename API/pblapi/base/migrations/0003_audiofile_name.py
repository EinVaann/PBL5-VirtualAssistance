# Generated by Django 4.0.4 on 2022-04-13 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_remove_audiofile_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='audiofile',
            name='name',
            field=models.CharField(default='NON', max_length=255),
            preserve_default=False,
        ),
    ]