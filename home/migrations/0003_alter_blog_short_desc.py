# Generated by Django 4.1.5 on 2023-01-25 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_blog_short_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='short_desc',
            field=models.CharField(default='', max_length=300),
        ),
    ]
