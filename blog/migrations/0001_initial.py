# Generated by Django 3.1.1 on 2020-09-29 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=44)),
                ('email', models.EmailField(max_length=55)),
                ('sms', models.CharField(max_length=444)),
            ],
        ),
    ]
