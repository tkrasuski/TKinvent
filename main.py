# -*- coding: utf-8 -*-
from Tkinter import *
from tkFileDialog import askopenfilename
import tkMessageBox as Msg
import helper as hlp
import json
talk = hlp.Talk()
service = '/default/service' 
class File_(object):
    '''
    taki prosty pojemnik na dane, mógłby być słownik ale to więcej pisania ;)
    '''
    def __init__(self):
        self.filename = None
        self.js = None # po prawdzie to jest to słownik

fl = File_()
window = Tk()
window.geometry('100x110+350+70')
def selectFile():
    fl.filename = askopenfilename(filetypes=[("Pliki JSON", "*.json")])
    file_label['text']=u'plik do wysłania: %s' %fl.filename
    file_label.pack()
    print fl.filename
    with open(fl.filename, 'rb') as fle:
        ftext = fle.read()
        # tu trzeba wstawić obsługe wyjątku json i wystawić jako błąd parsowania pliku
        fl.js=json.loads(ftext)
        text.insert(END,fl.js)
def sendFile():
    if fl.filename:
        for r in fl.js['content']:
            talk.data=r # iteracja po liście
            ret =talk.post_(service)
            print ret
    else:
        Msg.showinfo(u'Błąd', u'Wybierz plik przed wysłaniem.')
load_file_btn=Button(window, text=u'Załaduj plik', command=selectFile)
send_file_btn=Button(window, text=u'Wyślij plik', command=sendFile)
file_label = Label(window, text=u'plik do wysłania: %s' %fl.filename)
status_label = Label(window, text=u'Nie połączony')
text=Text(window, height=30, width=40)
scroll = Scrollbar(window, command=text.yview)
text.configure(yscrollcommand=scroll.set)
load_file_btn.pack()
send_file_btn.pack()
file_label.pack()
status_label.pack()
text.pack(side=LEFT)
scroll.pack(side=RIGHT, fill=Y)
window.mainloop()
