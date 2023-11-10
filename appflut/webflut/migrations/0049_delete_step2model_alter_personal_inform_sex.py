# Generated by Django 4.2.4 on 2023-11-08 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webflut', '0048_alter_step2model_sex'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Step2Model',
        ),
        migrations.AlterField(
            model_name='personal_inform',
            name='sex',
            field=models.CharField(choices=[('M', 'Мужчина'), ('F', 'Женщина'), ('', '')], default='', max_length=1),
        ),
    ]