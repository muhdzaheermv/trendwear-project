# Generated by Django 5.1.3 on 2025-01-02 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("virtualfitting", "0014_alter_usregister_email"),
    ]

    operations = [
        migrations.AddField(
            model_name="addproduct",
            name="email",
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
