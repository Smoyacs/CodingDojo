# Generated by Django 4.0.2 on 2022-02-24 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas_app', '0003_dojos_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dojos',
            name='desc',
            field=models.CharField(default='dojo antiguo', max_length=255),
        ),
    ]
