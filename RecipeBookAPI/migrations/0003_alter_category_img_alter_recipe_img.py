# Generated by Django 4.1.3 on 2023-09-14 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RecipeBookAPI', '0002_category_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='img',
            field=models.ImageField(upload_to='media/images'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='img',
            field=models.ImageField(upload_to='media/images'),
        ),
    ]
