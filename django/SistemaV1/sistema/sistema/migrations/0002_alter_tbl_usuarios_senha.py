# Generated by Django 5.1.2 on 2024-10-30 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_usuarios',
            name='senha',
            field=models.CharField(max_length=30),
        ),
    ]
