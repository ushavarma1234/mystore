# Generated by Django 4.2.7 on 2024-01-15 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Ecommerceapp", "0003_rename_description_sliders_description_1_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="rating",
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.DeleteModel(
            name="Rating",
        ),
    ]
