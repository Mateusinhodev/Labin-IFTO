# Generated by Django 5.0.7 on 2024-07-27 03:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agendamento', '0004_laboratorios_alter_agendamentos_laboratorio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='agendamentos',
            name='professor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='agendamento.professor'),
        ),
    ]
