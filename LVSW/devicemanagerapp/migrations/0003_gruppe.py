# Generated by Django 5.1 on 2024-12-01 01:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devicemanagerapp', '0002_hersteller_view'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gruppe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barcode', models.ForeignKey(db_column='Barcode', on_delete=django.db.models.deletion.CASCADE, related_name='gruppen_as_barcode', to='devicemanagerapp.barcodeelement')),
                ('gruppen_barcode', models.ForeignKey(db_column='GruppenBarcode', on_delete=django.db.models.deletion.CASCADE, related_name='gruppen_as_gruppenbarcode', to='devicemanagerapp.barcodeelement')),
            ],
        ),
    ]
