from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk import FreqDist
from re import match

# Hilffunktion für bereinigen von wörten wie "'s" aber wörter wie CO2,COVID-19 behalten 
def is_valid_token(token):
    return match(r'^[A-Za-z0-9\-]+$', token) is not None

class Text_bearbeiten:
    '''
    Dieses Modul bearbeitet Texte und erstellt Zusammenfassungen.
    '''
    def __init__(self,text,sprache,prozentsatz):
        self.text = text
        self.sprache = sprache
        self.prozentsatz = prozentsatz
        self.stopwords = set(stopwords.words(self.sprache))
        self.words = self.only_words()
        self.frequencies = self.word_count()
        self.sentences_score = self.sentences_count()
        self.summary = self.generate_summary(self.sentences_score)

    def only_words(self)->list:
        '''
        Gibt eine Liste mit den wichtigsten Wörter der Text zurück.
        Dabei wird der Text von Stopwords und Satzzeichen gereinigt. 
        '''
        words = word_tokenize(self.text)
       
        # Werden alle wörter aus dem Text, die nicht Stopwords oder Satzzeichen sind, geholt und in der liste geschrieben
        return [word.lower() for word in words if (w := word.lower()) and is_valid_token(w) and w not in punctuation and w not in self.stopwords]

    def word_count(self)->dict[str:float]:
        '''
        Gibt die normalisierten Häufigkeiten der Wörter zurück.
        Die Häufigkeiten werden durch den maximalen Wert geteilt und
        auf drei Nachkommastellen gerundet.
        '''
        # FreqDist gibt das Vorkommen für jedes Wort in der self.words Liste. Die self.words entspricht alle wichtige wörter des Textes 
        frequencies = dict(FreqDist(self.words))
        max_freq = max(frequencies.values(),default=1) # sicher stellen falls leerer text reinfliest 
        # Normlisieren 
        normalized = {word:round(freq/max_freq,3) for word,freq in frequencies.items()}
        return normalized
    def sentences_count(self)->dict[str:float]:
        '''
        Gibt den sentece count für jeden Satz, der im Text vorkommt zurück.
        Sentece count ist die Summe des Word counts, von jedem vorkommenden Wort.
        '''
        wort_count = self.frequencies
        sentences = sent_tokenize(self.text)
        # hier wird durch wort_count.get() überprüft ob wort in text und die summe von dennen pro Satz (durch for sentece in sentences) zurückgegeben
        sentence_count = {sentence: sum(wort_count.get(word.lower(), 0) for word in word_tokenize(sentence))for sentence in sentences}
        return sentence_count
    def generate_summary(self, sentence_count: dict[str, float]) -> str:
        '''
        Gibt eine Zusammenfassung, basierend auf den obersten 20% der bewerteten Sätze, zurück.
        '''
        # überprüfen ob sentece_count leer
        if not sentence_count:
            return ""
        # sicherstellen dass mindestens ein satzt das 20 % entspricht
        number_of_sentences = max(1, round(self.prozentsatz * len(sentence_count)))
        # Sortiere nach Score (absteigend), behalte nur die besten Sätze
        top_sentences = sorted(sentence_count.items(), key=lambda x: x[1], reverse=True)[:number_of_sentences]
        # Nur die Texte nehmen 
        top_sentences_texts = [s[0] for s in top_sentences]

        # Behalte Originalreihenfolge bei
        summary = [sentence for sentence in sent_tokenize(self.text) if sentence in top_sentences_texts]
        return ' '.join(summary)


        