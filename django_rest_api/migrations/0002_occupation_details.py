# Generated by Django 4.2.4 on 2023-08-31 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_rest_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Occupation_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profession', models.CharField(max_length=200)),
                ('company_name', models.CharField(max_length=200)),
                ('salary', models.IntegerField()),
            ],
        ),
    ]
