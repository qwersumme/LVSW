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


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
