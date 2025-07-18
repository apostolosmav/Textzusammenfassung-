from tkinter import *
from tkinter import filedialog,scrolledtext
from Text_bearbeitung import Text_bearbeiten
from tkinter import messagebox

class App(Tk):
    '''Klasse die ein Fenster initialisiert. Das Fenster enthält ein Scrolledtext Feld wo durch der "Import" Button, wird
       der Inhalt einer ausgewählte Textdatei durch Filedialog geschreiben und durch der "Text zusammenfassen" Button wird eine Zusammenfassung der Text geschrieben.
       Der Button "Manuelle Eingabe" gibt den Benutzer die möglichkeit den Text Manuelle zu übertragen, direkt schreiben oder hinzufügen.
    '''
    def __init__(self):
        Tk.__init__(self)
        self.title('Text zusammenfassen-App')

        # Label text
        self.label_text = Label (self,text='Text',font=('Ariel',12))
        self.label_text.grid(row=0,column=0,padx=10,sticky='w')

        # Widget Scrolledtext für das Text
        self.text = scrolledtext.ScrolledText(self)
        self.text.config(state='disabled',height=10,width=100,wrap=WORD,font=('Ariel',9))
        self.text.grid(row=1,column=0,padx=10,sticky='w')

        # Button Import
        self.bt_open_datei = Button(self,text='Import',font=('Ariel',9),command=self.open_file)
        self.bt_open_datei.grid(row=2,column=1,padx=10,pady=10,sticky='w')

        # Label Zusammenfassung 
        self.label_zusammenfassung = Label(self,text='Zusammenfassung generieren',font=('Ariel',12))
        self.label_zusammenfassung.grid(row=2,column=0,padx=10,sticky='w')

        # Button Manuelle Eingabe 
        self.bt_manuell = Button(self,text='Manuelle Eingabe',font=('Ariel',9),command=self.manuell)
        self.bt_manuell.grid(row=2,column=3,padx=10,pady=10,sticky='w')
        
        # Button Zusammenfassung generieren
        self.bt_zusammenfassen = Button(self,text='Zusammenfassung generieren',font=('Ariel',9),command=self.file_summary)
        self.bt_zusammenfassen.grid(row=2,column=4,padx=10,pady=10,sticky='w')

        # Widget Scrolledtext für die Zusammenfassung
        self.summary = scrolledtext.ScrolledText(self)
        self.summary.config(state='disabled',height=10,width=100,wrap=WORD,font=('Ariel',9))
        
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
        if len(text)>1: # überprüfen ob text noch leer ist 
            summary = Text_bearbeiten(text)
            self.summary.config(state='normal') # state ändern 
            self.summary.delete(1.0,END) # text Zusammenfassung erst mal bereinigen
            self.summary.insert(END,summary.summary) # Zusammenfassung ins Widget übergeben
            self.summary.grid(row=3,column=0,padx=10,sticky='w')
            self.summary.config(state='disabled') #state ändern damit der Benutzer die Zusammenfassung nicht beeinflüssen kann
        else:
            messagebox.showwarning('Wahrnung','Die Texteingabe ist leer.')

    def manuell(self):
        self.text.config(state='normal') # Manuelle eingabe erlauben

     
if __name__ == '__main__':
    App()
