# Generated by Django 4.2.4 on 2023-10-20 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webflut', '0017_alter_activities_add_product_delete_activities'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('calories_in', models.TextField()),
                ('time', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='activities_add',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webflut.activities'),
        ),
    ]
