# Generated by Django 4.1.3 on 2022-11-24 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_alter_review_grade'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='author',
            new_name='seller',
        ),
    ]