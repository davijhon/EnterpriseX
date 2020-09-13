# Generated by Django 3.0.7 on 2020-09-12 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('img', models.ImageField(upload_to='headers/')),
                ('position', models.CharField(choices=[('F', 'Firts'), ('S', 'Second'), ('T', 'Third')], max_length=1)),
                ('caption_title', models.CharField(blank=True, max_length=35, null=True)),
                ('caption_content', models.CharField(blank=True, max_length=65, null=True)),
                ('caption_button', models.URLField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]