# Generated by Django 2.1.2 on 2018-10-26 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misperris', '0003_auto_20181024_2117'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormJB',
            fields=[
                ('correo', models.CharField(max_length=15)),
                ('rut_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=15)),
                ('ingresar_fecha', models.DateTimeField(blank=True, null=True)),
                ('telefono', models.IntegerField(blank=True, null=True)),
                ('region', models.CharField(max_length=30)),
                ('ciudad', models.CharField(max_length=30)),
                ('tipo', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]