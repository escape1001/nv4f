# Generated by Django 5.0.2 on 2024-02-25 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Spot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('contents', models.TextField()),
                ('img_path', models.ImageField(blank=True, null=True, upload_to='spot/')),
                ('country', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('map_link', models.TextField()),
                ('member', models.CharField(max_length=50)),
                ('source', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
