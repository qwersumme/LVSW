# LVSW

### Projekt ausführen

Navigiere in den Unterordner
```
cd /LVSW/LVSW/

LVSW
├── DatabaseBackup
├── LVSW
| ├── bin
| ├── customermanagementapp
| ├── devicemanagerapp
| ├── eventmanagerapp
| ├── include
| ├── lib
| ├── lib64
| ├── LVSW
| ├── middleware
| ├── rentalapp
| ├── static
| ├── templates
| ├── db.sqlite3
| ├── manage.py (<- Das ist die Datei die verwendet werden muss)
| ├── pyvenv.cfg
README.md

```

Um das Django-Projekt lokal auszuführen, verwende den folgenden Befehl:

```bash
python manage.py runserver
```

Wenn die Anwendung von außen erreichbar sein soll, starte den Server mit:
```bash
python manage.py runserver 0.0.0.0:8000
```

### Benötigte Python-Bibliotheken

Für die Ausführung des Projekts müssen folgende Python-Bibliotheken installiert werden:

python-barcode & pillow:
```bash
pip install python-barcode pillow
```

mysqlclient:
```bash
pip install mysqlclient
```

builded nur dann wenn 
build_lvsw im commit enthalten ist


### TODOS
- Eventmanager
- Eventortmanager
- Gruppenerstellung
- Barcodestaten setzen anpassen, damit es ebenfalls mit Gruppen möglich ist
- Gruppen bearbeiten

- Benutzerverwaltung
