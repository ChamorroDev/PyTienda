# Generated by Django 4.2.1 on 2023-06-07 19:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=100)),
                ('numeracion', models.IntegerField(default=0)),
                ('ciudad', models.CharField(max_length=50)),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='direcciones', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Direccion',
                'verbose_name_plural': 'Direcciones',
                'unique_together': {('user', 'direccion', 'numeracion', 'ciudad')},
            },
        ),
    ]
