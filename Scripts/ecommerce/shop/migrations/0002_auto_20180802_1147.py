# Generated by Django 2.0.7 on 2018-08-02 02:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='ceated_at',
            new_name='created_at',
        ),
    ]