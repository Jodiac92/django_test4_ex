# Generated by Django 2.2.7 on 2019-11-18 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('irum', models.CharField(max_length=20)),
                ('juso', models.CharField(max_length=100)),
                ('nai', models.IntegerField()),
            ],
        ),
    ]
