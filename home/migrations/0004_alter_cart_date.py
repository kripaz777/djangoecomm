# Generated by Django 4.1.3 on 2022-12-02 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_cart"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cart",
            name="date",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
