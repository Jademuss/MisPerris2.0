# Generated by Django 2.1.2 on 2018-10-24 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misperris', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goku',
            old_name='descrip_rescatado',
            new_name='descripcion_rescatado',
        ),
        migrations.RemoveField(
            model_name='goku',
            name='img_rescatado',
        ),
        migrations.AddField(
            model_name='goku',
            name='imagen_rescatado',
            field=models.ImageField(blank=True, null=True, upload_to='lomito/%Y/%m/$d/'),
        ),
    ]
