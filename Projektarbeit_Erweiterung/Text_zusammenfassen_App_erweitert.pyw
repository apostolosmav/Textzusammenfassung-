from tkinter import *
from tkinter import filedialog,scrolledtext,ttk
from Text_bearbeitung_erweitert import Text_bearbeiten
from tkinter import messagebox
from langdetect import detect

class App(Tk):
    '''Klasse die ein Fenster initialisiert. Das Fenster enthält ein Scrolledtext Feld wo durch der "Import" Button, wird
       der Inhalt einer ausgewählte Textdatei durch Filedialog geschreiben und durch der "Text zusammenfassen" Button wird eine Zusammenfassung der Text geschrieben.
       Der Button "Manuelle Eingabe" gibt den Benutzer die möglichkeit den Text Manuelle zu übertragen, direkt schreiben oder hinzufügen.
    '''
    def __init__(self):
        Tk.__init__(self)
        self.title('Text zusammenfassen-App')

        # Label text
        self.label_text = LabelFrame(self,text='Text',font=('Ariel',12))
        self.label_text.grid(row=1,column=0,padx=10,pady=10,sticky='w')

        # Widget Scrolledtext für das Text
        self.text = scrolledtext.ScrolledText(self.label_text)
        self.text.config(state='disabled',height=10,width=100,wrap=WORD,font=('Ariel',9))
        self.text.grid(row=1,column=0,padx=10,sticky='w')

        # Label buttons
        self.label_buttons = LabelFrame(self,text='Buttons',font=('Ariel',12))
        self.label_buttons.grid(row=0,column=1,padx=10,pady=10,sticky='nw')

        # Button Import
        self.bt_open_datei = Button(self.label_buttons,text='Import',font=('Ariel',9),command=self.open_file)
        self.bt_open_datei.grid(row=0,column=0,padx=10,pady=10,sticky='w')

        # Button Manuelle Eingabe 
        self.bt_manuell = Button(self.label_buttons,text='Manuelle Eingabe',font=('Ariel',9),command=self.manuell)
        self.bt_manuell.grid(row=0,column=1,padx=10,pady=10,sticky='w')
        
        # Button Zusammenfassung generieren
        self.bt_zusammenfassen = Button(self.label_buttons,text='Zusammenfassung generieren',font=('Ariel',9),command=self.file_summary)
        self.bt_zusammenfassen.grid(row=0,column=2,padx=10,pady=10,sticky='w')

        # Button Text Löschen
        self.bt_leeren = Button(self.label_buttons,text='Text Löschen',font=('Ariel',9),command=self.loeschen)
        self.bt_leeren.grid(row=0,column=3,padx=10,pady=10,sticky='w')

        # Label Zusammenfassung 
        self.label_zusammenfassung = LabelFrame(self,text='Zusammenfassung',font=('Ariel',12))
       
 

        # Widget Scrolledtext für die Zusammenfassung
        self.zusammenfassung = scrolledtext.ScrolledText(self.label_zusammenfassung)
        self.zusammenfassung.config(state='disabled',height=10,width=100,wrap=WORD,font=('Ariel',9))
        
        #Label Comboboxen
        self.label_cb = LabelFrame(self,text='Sprache Auswahl und Prozentsatz',font=('Ariel',12))
        self.label_cb.grid(row=0,column=0,padx=10,pady=10,sticky='nw')

        # Combobox Sprache Auswahl
        self.sprache_auswahl = StringVar()
        self.cb_sprachen = ttk.Combobox(self.label_cb,textvariable=self.sprache_auswahl)
        self.cb_sprachen.grid(row=0,column=1,padx=10,pady=10,sticky='nw')
        self.cb_sprachen['values'] = ['Englisch','Deutsch','Griechisch']
        self.cb_sprachen['state'] = 'readonly'
        self.cb_sprachen.set('Englisch')

        # Combobox prozent der Zusammenfassung
        self.prozentsatz = StringVar(value=0.2)
        self.cb_prozentsatz = ttk.Combobox(self.label_cb,textvariable=self.prozentsatz)
        self.cb_prozentsatz.grid(row=0,column=1,padx=200,pady=10,sticky='nw')
        self.cb_prozentsatz['values'] = [0.2,0.3,0.4,0.5]
        self.cb_prozentsatz['state'] = 'readonly'

        # Label prozentsatz
        self.label_prozentsatz = Label(self.label_cb,text='Info:Prozentsatz entspricht der Prozentsatz der Schlüsselsätze des Texts\nFür längere Texte ist 0.2 Prozentsatz empfohlen und für kürzere Texte größer als 0.2',font=('Ariel',9))
        self.label_prozentsatz.grid(row=1,column=1,sticky='nw')

        self.mainloop()

    def open_file(self):
        self.text.config(state='normal') # state ändern, so dass wir in Text schreiben können
        file=filedialog.askopenfile('r',filetypes=[("all files", ".txt")]) # filedialog öffnen aber nur für files mit txt
        if file:
            daten = file.read() # Text aus dem file rausnehmen
            file.close() # file close 
            self.text.delete(1.0,END) # Text ein mal leeren 
            self.text.insert(END,daten) # Text ins Wiget übergeben
            self.text.config(state='disabled') # state ändern damit der Benutzer nicht den Text beeinflüssen kann

    def file_summary(self):
        text = self.text.get(1.0,END) # Text aus dem Widget nehmen
        if len(text)>1 : # überprüfen ob text noch leer ist 
            sprache = detect(text) # Sprach erkennen und die entsprechnde Values der Combobox zuweisen
            if sprache == 'en':
                sprache = 'Englisch'
            elif sprache == 'de':
                sprache = 'Deutsch'
            elif sprache == 'el':
                sprache = 'Griechisch'
            if  sprache == self.cb_sprachen.get(): # überprüfen ob Combobox auswahl und erkannte sprache der Text zusammenpasst
                # Spracheauswahl für nltk Verwendung umwandeln
                if sprache == 'Englisch':
                    sprache = 'english'
                elif sprache == 'Deutsch':
                    sprache = 'german'
                elif sprache == 'Griechisch':
                    sprache = 'greek'
                else: 
                    messagebox.showerror('Warnung','Die Sprache konnte nicht erkannt werden')
                    return
                zusammenfassung = Text_bearbeiten(text,sprache,float(self.cb_prozentsatz.get()))
                self.label_zusammenfassung.grid(row=2,column=0,padx=10,pady=10,sticky='w')
                self.zusammenfassung.config(state='normal') # state ändern 
                self.zusammenfassung.delete(1.0,END) # text Zusammenfassung erst mal bereinigen
                self.zusammenfassung.insert(END,zusammenfassung.summary) # Zusammenfassung ins Widget übergeben
                self.zusammenfassung.grid(row=3,column=0,padx=10,sticky='w')
                self.zusammenfassung.config(state='disabled') #state ändern damit der Benutzer die Zusammenfassung nicht beeinflüssen kann
            else:
                 messagebox.showwarning('Warnung','Die Texteingabe und Sprachauswahl stimmen nicht überein.')
        else:
            messagebox.showwarning('Warnung','Die Texteingabe ist leer.')

    def manuell(self):
        self.text.config(state='normal') # Manuelle eingabe erlauben
        self.text.delete(1.0,END)
        self.label_zusammenfassung.grid_forget() # Zusammenfassungs grid ausblenden aber nicht löschen

    
    def loeschen(self):
        self.text.config(state='normal') # Manuelle eingabe erlauben
        self.text.delete(1.0,END)
        self.label_zusammenfassung.grid_forget() # Zusammenfassungs grid ausblenden aber nicht löschen
        self.text.config(state='disabled')
     
if __name__ == '__main__':
    App()
