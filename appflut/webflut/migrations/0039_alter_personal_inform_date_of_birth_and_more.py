# Generated by Django 4.2.4 on 2023-10-30 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webflut', '0038_alter_personal_inform_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal_inform',
            name='date_of_birth',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='personal_inform',
            name='height',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='personal_inform',
            name='weight',
            field=models.FloatField(),
        ),
    ]
