# 📝 Automatische Textzusammenfassung mit Python

Dieses Projekt zeigt, wie man mithilfe klassischer NLP-Techniken automatisch lange Texte zusammenfassen kann. Die Methode basiert auf Satzähnlichkeiten (TF-IDF + Cosinus-Ähnlichkeit) und PageRank zur Gewichtung der wichtigsten Sätze.

---

## 📌 Ziel des Projekts

Ziel ist es, aus längeren Texten (z. B. Artikeln oder Berichten) automatisch die wichtigsten Kernaussagen zu extrahieren. Dadurch wird das schnelle Erfassen von Inhalten erleichtert – ganz ohne tiefergehendes Lesen des gesamten Textes.

---

## 🛠️ Verwendete Technologien

- Python 3
- Jupyter Notebook
- `nltk` – Textvorverarbeitung, Stopwords
- `scikit-learn` – TF-IDF-Vektorisierung, Cosine Similarity
- `networkx` – PageRank zur Gewichtung der Satzwichtigkeit
- `numpy`, `pandas` – Datenmanipulation
- `matplotlib` – Visualisierung

---

## 📁 Projektstruktur

Projektarbeit_Erweiterung/
│
├── Textzusammenfassung.ipynb # Hauptnotebook mit der kompletten Analyse
├── text.txt # Beispieltext für die Zusammenfassung
└── README.md # Projektdokumentation (diese Datei)


---

## 🔍 Methode Schritt für Schritt

1. **Text laden & in Sätze aufteilen**
2. **Satzbereinigung (Kleinbuchstaben, Stoppwörter entfernen, Tokenisierung)**
3. **TF-IDF-Vektoren für jeden Satz erstellen**
4. **Ähnlichkeitsmatrix zwischen Sätzen berechnen (Cosinus-Ähnlichkeit)**
5. **Graph konstruieren & PageRank anwenden**
6. **Top-N Sätze mit höchstem Score extrahieren**

---

## 📈 Beispielausgabe

**Originaltext:**  
Enthält z. B. 10 Sätze aus einem Artikel.

**Zusammenfassung (Top 3 Sätze):**  
- Satz 4  
- Satz 1  
- Satz 7  

Die extraktiven Sätze erscheinen in der Reihenfolge ihrer Wichtigkeit.

---

## ▶️ So kannst du das Projekt starten

### 🔧 Voraussetzungen

Installiere die benötigten Pakete mit:

```bash
pip install numpy pandas scikit-learn nltk matplotlib networkx
📚 NLTK vorbereiten
Führe im Notebook einmal folgenden Code aus, um die Stoppwörter herunterzuladen:

python
Kopieren
Bearbeiten
import nltk
nltk.download('punkt')
nltk.download('stopwords')
🚀 Notebook starten
Öffne das Jupyter Notebook Textzusammenfassung.ipynb und führe es schrittweise aus.

💡 Erweiterungsideen
GUI mit Tkinter oder Streamlit, um Texte dynamisch zusammenzufassen

Vergleich mit modernen Modellen wie BERT oder T5 (abstraktive Zusammenfassung)

Mehrsprachige Textverarbeitung (z. B. Deutsch, Englisch)

📌 GitHub: @apostolosmav

📄 Lizenz
Dieses Projekt ist unter der MIT License lizenziert.
