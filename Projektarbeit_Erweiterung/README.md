
# Text-Zusammenfassen-App

Dies ist eine benutzerfreundliche Desktop-Anwendung, mit der Benutzer Texte importieren, manuell eingeben und automatisch eine Zusammenfassung generieren können. Die Anwendung wurde mit **Tkinter** entwickelt und nutzt **NLTK** zur Textanalyse.

---

## Funktionen

- **Textimport aus .txt-Dateien:** Öffnen Sie Textdateien über einen Datei-Dialog.
- **Manuelle Eingabe:** Schreiben oder fügen Sie Texte direkt in das Eingabefeld ein.
- **Sprache automatisch erkennen:** Die Sprache des Textes wird erkannt und muss zur Auswahl in der ComboBox passen.
- **Sprachauswahl:** Unterstützt aktuell Deutsch, Englisch und Griechisch.
- **Prozentsatz der Zusammenfassung wählbar:** Wählen Sie, wie stark der Text komprimiert wird (20–50 %).
- **Zusammenfassung anzeigen:** Die wichtigsten Sätze des Textes werden angezeigt.
- **Text zurücksetzen:** Sowohl Eingabetext als auch Zusammenfassung können gelöscht werden.

---

## Technologien und Bibliotheken

- **Python 3.x**
- **Tkinter** – GUI
- **NLTK** – Textverarbeitung
- **langdetect** – automatische Spracherkennung

---

## Dateistruktur

```
├── Text_zusammenfassen_App_erweitert.pyw → Hauptskript (GUI)
├── Text_bearbeitung_erweitert.py → Kernmodul für Textverarbeitung
├── set_up_nltk.py → Setup-Skript zum Herunterladen von NLTK-Resourcen
└── README.md → Dieses Dokument
```

---

## Logik der Zusammenfassung

1. **Spracherkennung:** Das Programm erkennt automatisch die Sprache des eingegebenen Textes.
2. **Vorverarbeitung:**
   - Stopwörter und Satzzeichen werden entfernt
   - Wörter wie `CO2`, `COVID-19` bleiben erhalten
3. **Häufigkeitsanalyse:** Wörter werden nach Häufigkeit gewichtet.
4. **Satzbewertung:** Jeder Satz erhält einen Score basierend auf den enthaltenen wichtigen Wörtern.
5. **Top-Sätze auswählen:** Die besten Sätze (je nach gewähltem Prozentsatz) werden in Originalreihenfolge ausgegeben.

---

## Voraussetzungen

Installiere vor dem Ausführen folgende Pakete:

pip install nltk langdetect

Und lade in Python die benötigten NLTK-Ressourcen:
Einmalige ausführung das Set-up Skripts:
    python set_up_nltk.py
    Dieses Skript lädt:
    Tokenizer (punkt)
    Stoppwörter für: Englisch, Deutsch und Griechisch

---

## Ausführen

Starte die App mit:

```bash
python Text_zusammenfassen_App_erweitert.pyw
```

---

## Hinweise

- Die gewählte Sprache in der ComboBox **muss mit der erkannten Sprache übereinstimmen**, sonst erscheint eine Warnung.
- Für lange Texte ist ein niedriger Prozentsatz (z. B. 0.2) empfehlenswert.
- Das Programm unterstützt aktuell nur einfache `.txt`-Dateien.