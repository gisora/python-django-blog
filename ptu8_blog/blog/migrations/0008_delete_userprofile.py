# Generated by Django 4.1.7 on 2023-03-01 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_remove_comment_author_comment_commenter'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
