# Generated by Django 4.2.3 on 2023-07-25 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('electronics', '0002_table_gadgets'),
    ]

    operations = [
        migrations.RenameField(
            model_name='table_gadgets',
            old_name='g_image',
            new_name='photo',
        ),
    ]
