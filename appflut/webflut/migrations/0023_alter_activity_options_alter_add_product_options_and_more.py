# Generated by Django 4.2.4 on 2023-10-23 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webflut', '0022_alter_add_product_calories_in_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activity',
            options={'verbose_name': 'Виды Активностей ', 'verbose_name_plural': 'Виды Активностей'},
        ),
        migrations.AlterModelOptions(
            name='add_product',
            options={'verbose_name': 'Продукты Все', 'verbose_name_plural': 'Продукты Все'},
        ),
        migrations.AlterModelOptions(
            name='breakfast_products',
            options={'verbose_name': 'Продукты Завтрака', 'verbose_name_plural': 'Продукты Завтрака'},
        ),
        migrations.AlterModelOptions(
            name='dinner_products',
            options={'verbose_name': 'Продукты Ужина', 'verbose_name_plural': 'Продукты Ужина'},
        ),
        migrations.AlterModelOptions(
            name='lunch_products',
            options={'verbose_name': 'Продукты Обеда', 'verbose_name_plural': 'Продукты Обеда'},
        ),
        migrations.AlterModelOptions(
            name='personal_inform',
            options={'verbose_name': 'Личная Информация', 'verbose_name_plural': 'Личная Информация'},
        ),
        migrations.AlterModelOptions(
            name='snack_products',
            options={'verbose_name': 'Продукты Перекуса', 'verbose_name_plural': 'Продукты Перекуса'},
        ),
    ]
