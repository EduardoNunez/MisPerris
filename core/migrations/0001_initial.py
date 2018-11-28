# Generated by Django 2.1.2 on 2018-10-29 02:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_ciudad', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Ciudad',
                'verbose_name_plural': 'Ciudades',
            },
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genero_mascota', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_mascota', models.CharField(max_length=50)),
                ('fecha_Nacimiento_Mascota', models.DateField(null=True)),
                ('fecha_Ingreso', models.DateField(blank=True, null=True)),
                ('imagen_Mascota', models.FileField(blank=True, null=True, upload_to='media/')),
                ('estado_Mascota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Estado')),
                ('genero_mascota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Genero')),
            ],
        ),
        migrations.CreateModel(
            name='Postulante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correo_electronico', models.CharField(max_length=100)),
                ('run', models.CharField(max_length=12)),
                ('nombre_completo', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('telefono_contacto', models.IntegerField()),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Ciudad')),
            ],
        ),
        migrations.CreateModel(
            name='Raza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raza', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_region', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Region',
                'verbose_name_plural': 'Regiones',
            },
        ),
        migrations.CreateModel(
            name='Tipo_Vivienda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_tipoVivienda', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Tipo Vivienda',
                'verbose_name_plural': 'Tipo de Viviendas',
            },
        ),
        migrations.AddField(
            model_name='postulante',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Region'),
        ),
        migrations.AddField(
            model_name='postulante',
            name='tipo_vivienda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Tipo_Vivienda'),
        ),
        migrations.AddField(
            model_name='mascota',
            name='raza_mascota',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Raza'),
        ),
        migrations.AddField(
            model_name='ciudad',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Region'),
        ),
    ]
