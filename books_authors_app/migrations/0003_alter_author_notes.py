# Generated by Django 3.2.3 on 2021-06-14 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0002_author_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='notes',
            field=models.TextField(null=True),
        ),
    ]
