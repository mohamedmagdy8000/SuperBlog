# Generated by Django 2.2.5 on 2020-04-20 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200420_0451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.CharField(max_length=250, unique_for_date='publish'),
        ),
    ]
