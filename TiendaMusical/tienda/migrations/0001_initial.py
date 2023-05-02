# Generated by Django 4.2 on 2023-05-01 23:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FormatoDisco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'FormatoDisco',
                'verbose_name_plural': 'formatoDiscos',
            },
        ),
        migrations.CreateModel(
            name='Disco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('nombreAlbum', models.CharField(max_length=50)),
                ('precio', models.FloatField()),
                ('annopublicacion', models.DateField()),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='tienda')),
                ('oferta', models.BooleanField(default=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now_add=True)),
                ('formatos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.formatodisco')),
            ],
            options={
                'verbose_name': 'Disco',
                'verbose_name_plural': 'Discos',
            },
        ),
    ]
