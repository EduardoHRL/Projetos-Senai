# Generated by Django 5.1.2 on 2024-11-20 23:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_tarefa_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarefa',
            name='usuario',
        ),
    ]