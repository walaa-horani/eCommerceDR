# Generated by Django 4.2.7 on 2024-03-03 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commerceProDuct', '0003_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=True, upload_to='images'),
            preserve_default=False,
        ),
    ]