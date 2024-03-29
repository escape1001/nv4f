# Generated by Django 4.0.3 on 2024-03-27 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0002_alter_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='kr_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='city',
            name='kr_name',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='country',
            name='kr_name',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='district',
            name='kr_name',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='member',
            name='kr_name',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
