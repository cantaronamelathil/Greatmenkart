# Generated by Django 4.1.2 on 2022-11-18 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_variation_variation_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='variation_category',
            field=models.CharField(choices=[('color', 'Color'), ('size', 'size')], max_length=100),
        ),
    ]
