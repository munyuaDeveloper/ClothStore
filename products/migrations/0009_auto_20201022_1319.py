# Generated by Django 3.0 on 2020-10-22 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_product_subcategory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcategory',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='product_count',
        ),
        migrations.AddField(
            model_name='subcategory',
            name='slug',
            field=models.SlugField(default='Accessories', max_length=200, unique=True),
        ),
    ]
