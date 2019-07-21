# Generated by Django 2.2.3 on 2019-07-21 10:52

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('desription', models.TextField(blank=True, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to=main.models.content_file_name_artist)),
                ('logo', models.ImageField(blank=True, null=True, upload_to=main.models.content_file_name_artist_logo)),
                ('facebook', models.URLField(blank=True, null=True)),
                ('spotify', models.URLField(blank=True, null=True)),
                ('youtube', models.URLField(blank=True, null=True)),
                ('instagram', models.URLField(blank=True, null=True)),
                ('mail', models.CharField(max_length=128)),
                ('phone', models.CharField(max_length=128)),
            ],
        ),
    ]