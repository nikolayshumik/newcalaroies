# Generated by Django 4.2.4 on 2023-10-30 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webflut', '0042_alter_personal_inform_date_of_birth'),
    ]

    operations = [
        migrations.CreateModel(
            name='Step1Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Step2Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.CharField(choices=[('M', 'Мужчина'), ('F', 'Женщина')], default='M', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Step3Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.IntegerField(blank=True, null=True)),
                ('weight', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
