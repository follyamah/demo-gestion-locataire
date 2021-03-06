# Generated by Django 3.0.3 on 2020-04-04 08:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chambre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_chambre', models.CharField(blank=True, max_length=50, null=True)),
                ('nom', models.CharField(max_length=25)),
                ('prix', models.FloatField()),
                ('disponible', models.BooleanField(default=0)),
            ],
            options={
                'ordering': ['nom'],
                'permissions': (('peut voir chamnbre', 'Peut voir chambre'), ('peut voir detail chamnbre', 'Peut voir  detail chambre')),
            },
        ),
        migrations.CreateModel(
            name='Locataire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prenom_locataire', models.CharField(max_length=50)),
                ('nom_locataire', models.CharField(max_length=50)),
                ('contact_no', models.CharField(blank=True, max_length=15, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('email_address', models.EmailField(blank=True, max_length=254, null=True)),
            ],
            options={
                'ordering': ['prenom_locataire', 'nom_locataire'],
                'permissions': (('peut voir les locataires', 'Peut voir les locataires'),),
            },
        ),
        migrations.CreateModel(
            name='Maison',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('nom_maison', models.CharField(blank=True, max_length=150)),
                ('total_chambre', models.IntegerField()),
                ('quartier', models.CharField(blank=True, max_length=50)),
                ('photo_maison', models.ImageField(upload_to='')),
            ],
            options={
                'ordering': ['nom_maison'],
                'permissions': (('peut voir les maisons', 'Peut voir les maisons'),),
            },
        ),
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(default='images/staff.png', upload_to='utilisateur_img/')),
                ('prenom_utilisateur', models.CharField(max_length=50)),
                ('nom_utilisateur', models.CharField(max_length=50)),
                ('contact_no', models.CharField(max_length=15)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('email_address', models.EmailField(blank=True, max_length=254, null=True)),
                ('user', models.OneToOneField(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['prenom_utilisateur', 'nom_utilisateur'],
                'permissions': (('peut voir les utilisteurs', 'Peut voir les utilisteurs'), ('Peut voir le detail  des utilisteurs', 'Peut voir le detail  des utilistaurs')),
            },
        ),
        migrations.CreateModel(
            name='Payement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mois', models.CharField(choices=[('J', 'janvier'), ('F', 'fevrier'), ('M', 'mars'), ('A', 'avril'), ('M', 'mais'), ('J', 'juin'), ('J', 'juillet'), ('A', 'aout'), ('S', 'septembre'), ('O', 'octobre'), ('N', 'novembre'), ('N', 'novembre')], max_length=1)),
                ('montant', models.FloatField()),
                ('date_payement', models.DateTimeField(auto_now_add=True)),
                ('locataire', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Locataire')),
            ],
            options={
                'permissions': (('peut voir  payement', 'Peut voir payement'), ('peut voir detail des payements', 'Peut voir detail des payements')),
            },
        ),
        migrations.CreateModel(
            name='Contrat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_of_children', models.PositiveSmallIntegerField(default=0)),
                ('caution', models.FloatField()),
                ('no_of_adults', models.PositiveSmallIntegerField(default=1)),
                ('date_contrat', models.DateTimeField(default=django.utils.timezone.now)),
                ('expected_arrival_date_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('expected_departure_date_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('chambre_c', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Chambre')),
                ('locataire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Locataire')),
            ],
            options={
                'permissions': (('peut voir  contrat', 'Peut voir contrat'), ('peut voir detail des contrats', 'Peut voir detail des contrats')),
            },
        ),
        migrations.AddField(
            model_name='chambre',
            name='maison',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Maison'),
        ),
    ]
