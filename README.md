Fate Command Commander

Ein leichtgewichtiger, Python-basierter Kommandozeilen-Dateimanager (CLI), mit dem du dein Dateisystem direkt über das Terminal navigieren und verwalten kannst.
 Features

    Navigation: Wechsel zwischen Ordnern (go, back, home).

    Dateiverwaltung: Erstellen (make), Umbenennen (rename) und Löschen (del) von Verzeichnissen.

    Visualisierung: Auflisten von Dateien (ls) mit Filtern für nur Ordner (-o) oder nur Dateien (-d).

    Zwischenablage: Kopieren und Einfügen (copy/past) von Verzeichnissen inklusive Unterordnern.

    Programmstart: Dateien direkt mit Standardprogrammen aus dem Tool heraus öffnen.

 Voraussetzungen

Um dieses Tool zu nutzen, benötigst du lediglich:

    Python 3.10 oder höher (wegen der Verwendung von match/case Statements).

    Keine externen Bibliotheken erforderlich (nutzt ausschließlich die Python Standard Library).

 Befehlsübersicht
Befehl	Beschreibung
ls	Zeigt den Inhalt des aktuellen Verzeichnisses an.
ls -o / -d	Filtert die Anzeige nach Ordnern oder Dateien.
go [Pfad]	Wechselt in den angegebenen Unterordner.
back	Geht einen Ordner zurück.
make [Name]	Erstellt einen neuen Ordner.
copy [Name]	Speichert einen Ordner/Datei in den Zwischenspeicher.
past	Fügt den Inhalt aus dem Zwischenspeicher ein.
del [Name]	Löscht den angegebenen Ordner (mit Sicherheitsabfrage).
exit	Beendet das Programm.
