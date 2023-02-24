# Generated by Django 4.1.3 on 2023-02-24 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='date_created',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterUniqueTogether(
            name='song',
            unique_together={('name', 'artist')},
        ),
    ]
