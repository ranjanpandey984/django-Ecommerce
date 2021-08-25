# Generated by Django 3.2.6 on 2021-08-25 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_cart_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(blank=True, choices=[('active', 'active'), ('', 'inactive')], max_length=100),
        ),
        migrations.AlterField(
            model_name='slider',
            name='status',
            field=models.CharField(blank=True, choices=[('active', 'active'), ('', 'inactive')], max_length=100),
        ),
    ]
