# Generated by Django 2.2.11 on 2020-08-05 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200805_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='audio',
            field=models.CharField(max_length=150, verbose_name='audiofile path'),
        ),
    ]
