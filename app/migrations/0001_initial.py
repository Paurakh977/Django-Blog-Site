# Generated by Django 4.2.2 on 2023-07-04 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('desc', models.TextField()),
                ('slug', models.CharField(max_length=30)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
