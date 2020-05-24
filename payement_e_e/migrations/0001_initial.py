# Generated by Django 3.0.3 on 2020-05-16 15:08

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contrat', '0002_auto_20200516_1508'),
        ('chambre', '0003_auto_20200430_1120'),
    ]

    operations = [
        migrations.CreateModel(
            name='Annee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('annee', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Mois',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mois', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Payement_e_e',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant_eau', models.FloatField(blank=True, null=True)),
                ('montant_el', models.FloatField(blank=True, null=True)),
                ('date_payement', models.DateTimeField(default=django.utils.timezone.now)),
                ('annee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payement_e_e.Annee')),
                ('chambre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chambre.Chambre')),
                ('locataire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contrat.Contrat')),
                ('mois', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payement_e_e.Mois')),
            ],
            options={
                'ordering': ['locataire', 'annee', 'mois'],
                'permissions': (('peut voir  payement', 'Peut voir payement'), ('peut voir detail des payements', 'Peut voir detail des payements')),
            },
        ),
    ]
