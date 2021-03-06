# Generated by Django 3.0.3 on 2020-05-11 19:57

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chambre', '0003_auto_20200430_1120'),
        ('maison', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contrat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_locataire', models.CharField(blank=True, max_length=50)),
                ('prenom_locataire', models.CharField(max_length=50)),
                ('sexe', models.CharField(choices=[('M', 'Masculin'), ('F', 'Feminin')], max_length=1)),
                ('contact_no', models.CharField(blank=True, max_length=15, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('email_address', models.EmailField(blank=True, max_length=254, null=True)),
                ('caution', models.FloatField()),
                ('date_contrat', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_entree', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('date_sortie', models.DateTimeField()),
                ('profile_image', models.ImageField(upload_to='utilisateur_img/')),
                ('chambre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chambre.Chambre')),
                ('maison', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maison.Maison')),
            ],
            options={
                'permissions': (('peut voir  contrat', 'Peut voir contrat'), ('peut voir detail des contrats', 'Peut voir detail des contrats')),
            },
        ),
        migrations.CreateModel(
            name='LocataireInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('information', models.TextField(max_length=400)),
                ('locataire', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='contrat.Contrat')),
            ],
        ),
    ]
