# Generated by Django 5.0.3 on 2024-03-12 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['created_date']},
        ),
    ]
