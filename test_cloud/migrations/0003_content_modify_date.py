# Generated by Django 4.1.4 on 2023-01-21 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_cloud', '0002_content_author_alter_content_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='modify_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
