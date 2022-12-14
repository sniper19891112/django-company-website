# Generated by Django 2.2.11 on 2020-08-05 14:50

import careers.file_validation_field
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_article_audio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Speech',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=2000)),
                ('language', models.TextField(max_length=50)),
                ('file_name', models.TextField(max_length=1000)),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='audio',
            field=careers.file_validation_field.ContentTypeRestrictedFileField(help_text='Audio file auto generated .mp3', upload_to='articel/%Y/%m/%d/', verbose_name='Article Audio'),
        ),
    ]
