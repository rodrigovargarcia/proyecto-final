# Generated by Django 4.1.3 on 2023-01-02 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0005_mensaje_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensaje',
            name='email',
            field=models.EmailField(default='SOME STRING', max_length=20),
        ),
    ]
