# Generated by Django 4.1.5 on 2023-03-13 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_colorsizeproduct_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colorsizeproduct',
            name='color',
            field=models.CharField(max_length=100),
        ),
    ]
