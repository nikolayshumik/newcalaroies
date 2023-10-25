# Generated by Django 4.2.4 on 2023-10-23 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webflut', '0026_alter_personal_inform_goals_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal_inform',
            name='active',
            field=models.CharField(choices=[('L', 'Низкая активность'), ('M', 'Средняя активность'), ('H', 'Высокая активность')], default='L', max_length=1),
        ),
        migrations.AlterField(
            model_name='personal_inform',
            name='goals',
            field=models.CharField(choices=[('L', 'Похудение'), ('M', 'Набор массы'), ('F', 'Поддержание веса')], default='L', max_length=1),
        ),
    ]