# Generated by Django 5.0.6 on 2024-07-05 15:12

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('estoque', '0005_alter_material_qtd'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Requisition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('PENDENTE', 'Pendente'), ('APROVADA', 'Aprovada'), ('CANCELADA', 'Cancelada'), ('REPROVADA', 'Reprovada')], default='PENDENTE', max_length=100)),
                ('dateReq', models.DateTimeField(default=datetime.datetime.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RequisitionItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemQtd', models.IntegerField()),
                ('itemMat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estoque.material')),
                ('itemReq', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requisition.requisition')),
            ],
        ),
        migrations.AddField(
            model_name='requisition',
            name='items',
            field=models.ManyToManyField(through='requisition.RequisitionItem', to='estoque.material'),
        ),
    ]
