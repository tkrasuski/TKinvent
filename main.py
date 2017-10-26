# -*- coding: utf-8 -*-
from Tkinter import *
from tkFileDialog import askopenfilename
import tkMessageBox as Msg
import helper as hlp
import json
talk = hlp.Talk()
service = '/default/service' 
# obsłuż wyjątek !!!
rfs=talk.get_(service)
load_id=rfs['result']['load_id']

class File_(object):
    '''
    taki prosty pojemnik na dane, mógłby być słownik ale to więcej pisania ;)
    '''
    def __init__(self):
        self.filename = None
        self.js = None # po prawdzie to jest to słownik
        self.load_id = None

fl = File_()
fl.load_id = load_id
window = Tk()
window.geometry('650x500+300+300')
def selectFile():
    fl.filename = askopenfilename(filetypes=[("Pliki JSON", "*.json")])
    file_label['text']=u'plik do wysłania: %s' %fl.filename
    file_label.pack()
    print fl.filename
    with open(fl.filename, 'rb') as fle:
        ftext = fle.read()
        # tu trzeba wstawić obsługe wyjątku json i wystawić jako błąd parsowania pliku
        fl.js=json.loads(ftext)
        #text.insert(END,fl.js)
def sendFile():
    status_label['text']=u'łączę..'
    if fl.filename:
        
        for r in fl.js['content']:
            status_label['text']=u'wysyłam linię %s'% str(r)
            talk.data=dict(load_id=fl.load_id, line=r['line']) # iteracja po liście
            ret =talk.post_(service)
            print ret
            text.insert(END,'\n Wysłano:')
            text.insert(END,talk.data)
            text.insert(END,'\n Odpowiedź serwera:')
            text.insert(END,ret)
    else:
        status_label['text']=u'błąd'
        Msg.showinfo(u'Błąd', u'Wybierz plik przed wysłaniem.')
    status_label['text']=u'nie połączony'
load_file_btn=Button(window, text=u'Załaduj plik', command=selectFile)
send_file_btn=Button(window, text=u'Wyślij plik', command=sendFile)
file_label = Label(window, text=u'plik do wysłania: %s' %fl.filename)
status_label = Label(window, text=u'Nie połączony')
text=Text(window, height=30, width=80)
scroll = Scrollbar(window, command=text.yview)
text.configure(yscrollcommand=scroll.set)
load_file_btn.pack(side=TOP)
send_file_btn.pack(side=TOP)
file_label.pack(side=TOP)
status_label.pack(side=TOP)
text.pack(side=LEFT)
scroll.pack(side=RIGHT, fill=Y)
window.mainloop()
