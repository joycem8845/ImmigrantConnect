# Generated by Django 2.1.2 on 2018-10-14 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_auto_20181014_0155'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employer', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('email', models.EmailField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
                ('ad', models.BooleanField(default=False)),
            ],
        ),
    ]
