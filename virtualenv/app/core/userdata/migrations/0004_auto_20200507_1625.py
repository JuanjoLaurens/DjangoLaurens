# Generated by Django 2.2 on 2020-05-07 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0003_auto_20200507_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habilidades',
            name='DescHabil',
            field=models.TextField(max_length=2000, verbose_name='Descripcioón de la habilidad'),
        ),
    ]
