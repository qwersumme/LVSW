# Generated by Django 5.1 on 2024-11-18 00:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Barcodeelement',
            fields=[
                ('barcode', models.AutoField(db_column='Barcode', primary_key=True, serialize=False)),
                ('kaufdatum', models.DateField(blank=True, db_column='Kaufdatum', null=True)),
                ('bemerkungen', models.TextField(blank=True, db_column='Bemerkungen', null=True)),
                ('istgruppe', models.IntegerField(blank=True, db_column='IstGruppe', null=True)),
                ('zustand', models.CharField(blank=True, db_column='Zustand', max_length=12, null=True)),
                ('länge', models.DecimalField(blank=True, db_column='Länge', decimal_places=2, max_digits=10, null=True)),
                ('breite', models.DecimalField(blank=True, db_column='Breite', decimal_places=2, max_digits=10, null=True)),
                ('höhe', models.DecimalField(blank=True, db_column='Höhe', decimal_places=2, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'BarcodeElement',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Eventort',
            fields=[
                ('eventortid', models.IntegerField(db_column='EventOrtID', primary_key=True, serialize=False)),
                ('bezeichnung', models.CharField(blank=True, db_column='Bezeichnung', max_length=100, null=True)),
                ('strassehausnummer', models.CharField(blank=True, db_column='StrasseHausnummer', max_length=100, null=True)),
                ('plz', models.CharField(blank=True, db_column='PLZ', max_length=10, null=True)),
                ('stadt', models.CharField(blank=True, db_column='Stadt', max_length=50, null=True)),
                ('notizen', models.TextField(blank=True, db_column='Notizen', null=True)),
            ],
            options={
                'db_table': 'EventOrt',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('eventid', models.IntegerField(db_column='EventID', primary_key=True, serialize=False)),
                ('bezeichnung', models.CharField(blank=True, db_column='Bezeichnung', max_length=100, null=True)),
                ('startdatum', models.DateField(blank=True, db_column='Startdatum', null=True)),
                ('enddatum', models.DateField(blank=True, db_column='Enddatum', null=True)),
                ('notizen', models.TextField(blank=True, db_column='Notizen', null=True)),
            ],
            options={
                'db_table': 'Events',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Geraetetyp',
            fields=[
                ('gerätetypid', models.IntegerField(db_column='GerätetypID', primary_key=True, serialize=False)),
                ('modellbezeichnung', models.CharField(blank=True, db_column='Modellbezeichnung', max_length=100, null=True)),
                ('kategorie', models.CharField(blank=True, db_column='Kategorie', max_length=50, null=True)),
                ('anleitungslink', models.TextField(blank=True, db_column='Anleitungslink', null=True)),
                ('gewicht', models.DecimalField(blank=True, db_column='Gewicht', decimal_places=2, max_digits=10, null=True)),
                ('länge', models.DecimalField(blank=True, db_column='Länge', decimal_places=2, max_digits=10, null=True)),
                ('breite', models.DecimalField(blank=True, db_column='Breite', decimal_places=2, max_digits=10, null=True)),
                ('höhe', models.DecimalField(blank=True, db_column='Höhe', decimal_places=2, max_digits=10, null=True)),
                ('kaufpreis', models.DecimalField(blank=True, db_column='Kaufpreis', decimal_places=2, max_digits=10, null=True)),
                ('vermietpreis', models.DecimalField(blank=True, db_column='Vermietpreis', decimal_places=2, max_digits=10, null=True)),
                ('mengenrabatt', models.DecimalField(blank=True, db_column='Mengenrabatt', decimal_places=2, max_digits=10, null=True)),
                ('zubehör', models.TextField(blank=True, db_column='Zubehör', null=True)),
                ('notizen', models.TextField(blank=True, db_column='Notizen', null=True)),
            ],
            options={
                'db_table': 'Geraetetyp',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Hersteller',
            fields=[
                ('herstellerid', models.IntegerField(db_column='HerstellerID', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=100, null=True)),
            ],
            options={
                'db_table': 'Hersteller',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Kunde',
            fields=[
                ('kundenid', models.IntegerField(db_column='KundenID', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=100, null=True)),
                ('email', models.CharField(blank=True, db_column='Email', max_length=100, null=True)),
                ('telefon', models.CharField(blank=True, db_column='Telefon', max_length=20, null=True)),
                ('mobil', models.CharField(blank=True, db_column='Mobil', max_length=20, null=True)),
                ('strassehausnummer', models.CharField(blank=True, db_column='StrasseHausnummer', max_length=100, null=True)),
                ('plz', models.CharField(blank=True, db_column='PLZ', max_length=10, null=True)),
                ('stadt', models.CharField(blank=True, db_column='Stadt', max_length=50, null=True)),
                ('notizen', models.TextField(blank=True, db_column='Notizen', null=True)),
            ],
            options={
                'db_table': 'Kunde',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Lagerort',
            fields=[
                ('lagerortid', models.AutoField(db_column='LagerortID', primary_key=True, serialize=False)),
                ('strassehausnummer', models.CharField(blank=True, db_column='StrasseHausnummer', max_length=255, null=True)),
                ('plz', models.CharField(blank=True, db_column='PLZ', max_length=5, null=True)),
                ('stadt', models.CharField(blank=True, db_column='Stadt', max_length=255, null=True)),
                ('bemerkungen', models.TextField(blank=True, db_column='Bemerkungen', null=True)),
                ('regalkennung', models.CharField(blank=True, db_column='Regalkennung', max_length=255, null=True)),
            ],
            options={
                'db_table': 'Lagerort',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BarcodeEvent',
            fields=[
                ('barcode', models.OneToOneField(db_column='Barcode', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='rentalapp.barcodeelement')),
            ],
            options={
                'db_table': 'Barcode_Event',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BarcodeLagerort',
            fields=[
                ('barcode', models.OneToOneField(db_column='Barcode', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='rentalapp.barcodeelement')),
            ],
            options={
                'db_table': 'Barcode_Lagerort',
                'managed': False,
            },
        ),
    ]
