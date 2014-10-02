# -*- coding: utf-8 -*-
from evernote.api.client import EvernoteClient
import evernote.edam.type.ttypes as Types
import evernote.edam.userstore.constants as UserStoreConstants

dev_token="S=s1:U=8eed8:E=14e51eeb245:C=146fa3d8410:P=1cd:A=en-devtoken:V=2:H=0daa91a172de827575a961a42c4d20b4"
client = EvernoteClient(token=dev_token)
userStore = client.get_user_store()
user = userStore.getUser()
print user.username

noteStore = client.get_note_store()
notebooks = noteStore.listNotebooks()
for n in notebooks:
    print n.name
#upload a note
noteStore = client.get_note_store()
note = Types.Note()
note.title = "I'm a test note 2!"
note.content = '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd">'
note.content += '<en-note>Hello, world!</en-note>'
#note = noteStore.createNote(note)
print note
#create a notebook
notebook = Types.Notebook()
notebook.name = "My Notebook我的東西haha"
notebook = noteStore.createNotebook(notebook)
print notebook.guid

