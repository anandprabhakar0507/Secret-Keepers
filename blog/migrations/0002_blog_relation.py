# Generated by Django 3.1.3 on 2020-11-05 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='relation',
            field=models.CharField(default='gk', max_length=100),
            preserve_default=False,
        ),
    ]
