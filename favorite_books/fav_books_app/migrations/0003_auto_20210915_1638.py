# Generated by Django 2.2 on 2021-09-15 21:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fav_books_app', '0002_auto_20210915_1516'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='user_uploads',
            new_name='uploaded_by',
        ),
    ]