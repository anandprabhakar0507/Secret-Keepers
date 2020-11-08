# Generated by Django 3.1.3 on 2020-11-07 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_blog_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sn', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=200)),
                ('phone', models.TextField(max_length=13)),
                ('message', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='files/')),
            ],
        ),
    ]