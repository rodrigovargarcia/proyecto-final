# Generated by Django 4.1.3 on 2022-12-30 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imagen',
            field=models.ImageField(blank=True, null='True', upload_to='posteos'),
            preserve_default='True',
        ),
    ]
