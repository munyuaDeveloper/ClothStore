# Generated by Django 3.0 on 2020-10-22 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20201022_0731'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subcategory',
            options={'ordering': ('name',), 'verbose_name': 'sub category', 'verbose_name_plural': 'sub categories'},
        ),
    ]
