# Generated by Django 2.1.5 on 2019-02-15 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pvn',
            field=models.PositiveSmallIntegerField(default=21),
        ),
    ]
