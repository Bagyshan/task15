# Generated by Django 5.0 on 2023-12-17 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ManyToManyApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='human',
            name='bus',
            field=models.ManyToManyField(related_query_name='humans', to='ManyToManyApp.bus'),
        ),
    ]
