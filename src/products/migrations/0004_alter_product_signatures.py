# Generated by Django 4.1.5 on 2023-03-12 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_description_alter_product_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='signatures',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
