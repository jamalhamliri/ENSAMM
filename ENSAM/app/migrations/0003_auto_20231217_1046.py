# Generated by Django 3.1.14 on 2023-12-17 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20231215_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='description',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='article',
            name='fichier',
            field=models.FileField(blank=True, upload_to='media/fichier/'),
        ),
    ]