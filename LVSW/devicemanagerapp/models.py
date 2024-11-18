from django.db import models

# Create your models here.

#INSERT INTO `Hersteller` (`Name`) VALUES ('Generic'), ('Futurelight'), ('Robe'), ('Martin'),('JBLighting')

#ALTER TABLE `Geraetetyp` DROP FOREIGN KEY `fk_Hersteller`;
#ALTER TABLE `Hersteller` CHANGE `HerstellerID` `HerstellerID` INT(11) NOT NULL AUTO_INCREMENT;
#ALTER TABLE `Geraetetyp` ADD CONSTRAINT `fk_Hersteller` FOREIGN KEY (`HerstellerID`) REFERENCES `Hersteller` (`HerstellerID`);


# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Barcodeelement(models.Model):
    barcode = models.AutoField(db_column='Barcode', primary_key=True)  # Field name made lowercase.
    geraetetypid = models.ForeignKey('Geraetetyp', models.DO_NOTHING, db_column='GeraetetypID')  # Field name made lowercase.
    kaufdatum = models.DateField(db_column='Kaufdatum', blank=True, null=True)  # Field name made lowercase.
    bemerkungen = models.TextField(db_column='Bemerkungen', blank=True, null=True)  # Field name made lowercase.
    istgruppe = models.IntegerField(db_column='IstGruppe', blank=True, null=True)  # Field name made lowercase.
    zustand = models.CharField(db_column='Zustand', max_length=12, blank=True, null=True)  # Field name made lowercase.
    länge = models.DecimalField(db_column='Länge', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    breite = models.DecimalField(db_column='Breite', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    höhe = models.DecimalField(db_column='Höhe', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BarcodeElement'


class BarcodeEvent(models.Model):
    barcode = models.OneToOneField(Barcodeelement, models.DO_NOTHING, db_column='Barcode', primary_key=True)  # Field name made lowercase. The composite primary key (Barcode, EventID) found, that is not supported. The first column is selected.
    eventid = models.ForeignKey('Events', models.DO_NOTHING, db_column='EventID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Barcode_Event'
        unique_together = (('barcode', 'eventid'),)


class BarcodeLagerort(models.Model):
    barcode = models.OneToOneField(Barcodeelement, models.DO_NOTHING, db_column='Barcode', primary_key=True)  # Field name made lowercase. The composite primary key (Barcode, LagerortID) found, that is not supported. The first column is selected.
    lagerortid = models.ForeignKey('Lagerort', models.DO_NOTHING, db_column='LagerortID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Barcode_Lagerort'
        unique_together = (('barcode', 'lagerortid'),)


class Eventort(models.Model):
    eventortid = models.IntegerField(db_column='EventOrtID', primary_key=True)  # Field name made lowercase.
    bezeichnung = models.CharField(db_column='Bezeichnung', max_length=100, blank=True, null=True)  # Field name made lowercase.
    strassehausnummer = models.CharField(db_column='StrasseHausnummer', max_length=100, blank=True, null=True)  # Field name made lowercase.
    plz = models.CharField(db_column='PLZ', max_length=10, blank=True, null=True)  # Field name made lowercase.
    stadt = models.CharField(db_column='Stadt', max_length=50, blank=True, null=True)  # Field name made lowercase.
    notizen = models.TextField(db_column='Notizen', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EventOrt'


class Events(models.Model):
    eventid = models.IntegerField(db_column='EventID', primary_key=True)  # Field name made lowercase.
    eventortid = models.ForeignKey(Eventort, models.DO_NOTHING, db_column='EventOrtID')  # Field name made lowercase.
    kundenid = models.ForeignKey('Kunde', models.DO_NOTHING, db_column='KundenID')  # Field name made lowercase.
    bezeichnung = models.CharField(db_column='Bezeichnung', max_length=100, blank=True, null=True)  # Field name made lowercase.
    startdatum = models.DateField(db_column='Startdatum', blank=True, null=True)  # Field name made lowercase.
    enddatum = models.DateField(db_column='Enddatum', blank=True, null=True)  # Field name made lowercase.
    notizen = models.TextField(db_column='Notizen', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Events'


class Geraetetyp(models.Model):
    gerätetypid = models.IntegerField(db_column='GerätetypID', primary_key=True)  # Field name made lowercase.
    herstellerid = models.ForeignKey('Hersteller', models.DO_NOTHING, db_column='HerstellerID')  # Field name made lowercase.
    modellbezeichnung = models.CharField(db_column='Modellbezeichnung', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kategorie = models.CharField(db_column='Kategorie', max_length=50, blank=True, null=True)  # Field name made lowercase.
    anleitungslink = models.TextField(db_column='Anleitungslink', blank=True, null=True)  # Field name made lowercase.
    gewicht = models.DecimalField(db_column='Gewicht', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    länge = models.DecimalField(db_column='Länge', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    breite = models.DecimalField(db_column='Breite', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    höhe = models.DecimalField(db_column='Höhe', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    kaufpreis = models.DecimalField(db_column='Kaufpreis', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vermietpreis = models.DecimalField(db_column='Vermietpreis', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    mengenrabatt = models.DecimalField(db_column='Mengenrabatt', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    zubehör = models.TextField(db_column='Zubehör', blank=True, null=True)  # Field name made lowercase.
    notizen = models.TextField(db_column='Notizen', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Geraetetyp'


class Hersteller(models.Model):
    #herstellerid = models.IntegerField(db_column='HerstellerID', primary_key=True)  # Field name made lowercase.
    id = models.AutoField(primary_key=True)
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Hersteller'

class Hersteller_view(models.Model):
    herstellerid = models.IntegerField(db_column='HerstellerID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Hersteller'


class Kunde(models.Model):
    kundenid = models.IntegerField(db_column='KundenID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=100, blank=True, null=True)  # Field name made lowercase.
    telefon = models.CharField(db_column='Telefon', max_length=20, blank=True, null=True)  # Field name made lowercase.
    mobil = models.CharField(db_column='Mobil', max_length=20, blank=True, null=True)  # Field name made lowercase.
    strassehausnummer = models.CharField(db_column='StrasseHausnummer', max_length=100, blank=True, null=True)  # Field name made lowercase.
    plz = models.CharField(db_column='PLZ', max_length=10, blank=True, null=True)  # Field name made lowercase.
    stadt = models.CharField(db_column='Stadt', max_length=50, blank=True, null=True)  # Field name made lowercase.
    notizen = models.TextField(db_column='Notizen', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Kunde'

class Lagerort(models.Model):
    lagerortid = models.AutoField(db_column='LagerortID', primary_key=True)  # Field name made lowercase.
    strassehausnummer = models.CharField(db_column='StrasseHausnummer', max_length=255, blank=True, null=True)  # Field name made lowercase.
    plz = models.CharField(db_column='PLZ', max_length=5, blank=True, null=True)  # Field name made lowercase.
    stadt = models.CharField(db_column='Stadt', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bemerkungen = models.TextField(db_column='Bemerkungen', blank=True, null=True)  # Field name made lowercase.
    regalkennung = models.CharField(db_column='Regalkennung', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Lagerort'

