# Generated by Django 2.2 on 2020-05-13 22:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userdata', '0006_auto_20200513_1745'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategProye',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lenguaje', models.CharField(max_length=255, verbose_name='Lenguaje que se utlizo en el proyecto')),
                ('motorDB', models.CharField(max_length=255, verbose_name='Motor de base de datos utilizado en el proyecto')),
                ('arquitectura', models.CharField(max_length=255, verbose_name='Arquitectura del proyecto')),
            ],
            options={
                'verbose_name': 'Categorias de los proyectos',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='TipoDocu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombTipoDoc', models.CharField(max_length=255, verbose_name='Nombre del tipo de proyecto')),
            ],
            options={
                'verbose_name': 'Tipo de documentos de los proyectos',
                'verbose_name_plural': 'Tipos de proyecto',
            },
        ),
        migrations.CreateModel(
            name='Proyects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombProyec', models.CharField(max_length=255, verbose_name='Nombre del Proyecto')),
                ('descProyec', models.CharField(max_length=255, verbose_name='Descripción del proyecto')),
                ('imgProyec', models.CharField(default='user.png', max_length=255, verbose_name='Imagen Del proyecto')),
                ('urlRepo', models.CharField(max_length=100, verbose_name='Link del repositorio')),
                ('fechaInicio', models.DateTimeField(verbose_name='Fue iniciado el')),
                ('fechaFinal', models.DateTimeField(verbose_name='Fue terminado el')),
                ('statusProjecto', models.CharField(max_length=255, verbose_name='Estado del proyecto')),
                ('idCateProyec', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portafolio.CategProye', verbose_name='Identificación de la categoria del proyecto')),
            ],
            options={
                'verbose_name': 'Projectos de los usuarios',
                'verbose_name_plural': 'Projectos',
            },
        ),
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombDocu', models.CharField(max_length=255, verbose_name='Nombre del Documento')),
                ('pathDocu', models.CharField(max_length=255, verbose_name='Ruta del documento')),
                ('idProyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portafolio.Proyects', verbose_name='Identificación del proyecto')),
                ('idTipoDocu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portafolio.TipoDocu', verbose_name='Identificación del tipo de proyecto')),
                ('idUsuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userdata.DatosUser', verbose_name='Identificación del usuario')),
            ],
            options={
                'verbose_name': 'Documentos del proyecto',
                'verbose_name_plural': 'Documentos',
            },
        ),
    ]
