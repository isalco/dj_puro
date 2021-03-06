# Generated by Django 3.0.3 on 2020-03-04 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dj_puro', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoria',
            options={'verbose_name_plural': 'Categorías'},
        ),
        migrations.RemoveField(
            model_name='categoria',
            name='activo',
        ),
        migrations.AlterField(
            model_name='categoria',
            name='descripcion',
            field=models.CharField(help_text='Descripción de la Categoría', max_length=100, unique=True),
        ),
        migrations.CreateModel(
            name='SubCategoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(help_text='Descripción de la Sub Categoría', max_length=100)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dj_puro.Categoria')),
            ],
            options={
                'verbose_name_plural': 'Sub Categorías',
                'unique_together': {('categoria', 'descripcion')},
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(help_text='Descripción del Producto', max_length=100, unique=True)),
                ('fecha_creado', models.DateTimeField()),
                ('vendido', models.BooleanField(default=False)),
                ('subcategoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dj_puro.SubCategoria')),
            ],
            options={
                'verbose_name_plural': 'Productos',
            },
        ),
    ]
