# Generated by Django 3.1.3 on 2020-11-07 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_blog_short_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='Short_Description',
            field=models.TextField(max_length=400),
        ),
    ]