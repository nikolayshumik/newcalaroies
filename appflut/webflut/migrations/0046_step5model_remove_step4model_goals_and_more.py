# Generated by Django 4.2.4 on 2023-11-08 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webflut', '0045_steptestmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Step5Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goals', models.CharField(choices=[('L', 'Похудение'), ('M', 'Набор массы'), ('F', 'Поддержание веса')], default='L', max_length=1)),
            ],
        ),
        migrations.RemoveField(
            model_name='step4model',
            name='goals',
        ),
        migrations.AlterField(
            model_name='step4model',
            name='active',
            field=models.CharField(choices=[('L', 'малоактивный'), ('M', 'активный')], default='L', max_length=1),
        ),
    ]
