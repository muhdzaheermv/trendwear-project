# Generated by Django 4.2.16 on 2024-12-16 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('virtualfitting', '0008_alter_addproduct_productid_alter_addproduct_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addproduct',
            name='productid',
        ),
    ]
