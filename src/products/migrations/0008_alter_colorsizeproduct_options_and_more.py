# Generated by Django 4.1.5 on 2023-03-13 04:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_rename_product_baseproduct_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='colorsizeproduct',
            options={'ordering': ['name']},
        ),
        migrations.RemoveField(
            model_name='colorsizeproduct',
            name='product',
        ),
        migrations.AddField(
            model_name='colorsizeproduct',
            name='brand',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='colorsizeproduct',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='colorsizeproduct',
            name='name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='colorsizeproduct',
            name='signatures',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='colorsizeproduct',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.DeleteModel(
            name='BaseProduct',
        ),
    ]
