# Generated by Django 5.1.4 on 2025-02-01 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('virtualfitting', '0021_alter_addproduct_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addproduct',
            name='size',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
