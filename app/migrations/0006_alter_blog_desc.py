# Generated by Django 4.2.2 on 2023-07-04 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_blog_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='desc',
            field=models.TextField(),
        ),
    ]