# Generated by Django 2.1.3 on 2018-11-20 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='news_date',
            field=models.TextField(blank=True),
        ),
    ]
