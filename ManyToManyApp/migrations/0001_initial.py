# Generated by Django 5.0 on 2023-12-17 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('busnumber', models.IntegerField()),
                ('busmodel', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Human',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('sex', models.CharField(choices=[('male', 'мужской'), ('female', 'женский')], max_length=20)),
                ('bus', models.ManyToManyField(related_name='humans', to='ManyToManyApp.bus')),
            ],
        ),
    ]
