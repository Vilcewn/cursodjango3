# Generated by Django 4.2.2 on 2023-06-25 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_post_approved'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='approved',
            new_name='deleted',
        ),
    ]