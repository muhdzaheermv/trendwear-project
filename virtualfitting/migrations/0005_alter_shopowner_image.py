# Generated by Django 5.1.3 on 2024-11-30 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('virtualfitting', '0004_shopowner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopowner',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='shop/'),
        ),
    ]
