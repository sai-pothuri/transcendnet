# Generated by Django 3.1.3 on 2020-11-26 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WeeklyBulletin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='category',
            field=models.CharField(choices=[('ed', 'Editorial'), ('sc', 'Science'), ('bs', 'Business'), ('ls', 'Leisure'), ('sp', 'Sports'), ('nw', 'News')], default='ed', max_length=2),
        ),
    ]
