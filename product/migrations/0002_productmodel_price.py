# Generated by Django 4.0.10 on 2023-02-27 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1.0, max_digits=5),
        ),
    ]
