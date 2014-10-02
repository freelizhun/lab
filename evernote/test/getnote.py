import evernote.edam.type.ttypes as Types
import evernote.edam.notestore.ttypes as NoteStore

from evernote.api.client import EvernoteClient

auth_token = "S=s1:U=8eed8:E=14e51eeb245:C=146fa3d8410:P=1cd:A=en-devtoken:V=2:H=0daa91a172de827575a961a42c4d20b4"

def list_notes(notebook_guid, user_store, note_store):
    note_filter = NoteStore.NoteFilter()
    note_filter.notebookGuid = notebook_guid
    notes = note_store.findNotes(auth_token,
                                 note_filter, 0, 100).notes
    notes_lst = []
    for note in notes:
        this_note = {'NoteTitle': note.title, 'NoteId': note.guid}
        notes_lst.append(this_note)

    return notes_lst

def list_notebooks(note_store):
    nb=[]
    notebooks = note_store.listNotebooks()
    for n in notebooks:
        print n.guid, n.name
        nb.append(n.guid)
    return nb

def get_note_content(note_guid, note_store):
    note_content = note_store.getNote(note_guid, True, False, False, False)
    return note_content

def get_guid_from_notename(nbs, notename):
    notes = list_notes(nbs[0], 'empty', note_store)
    print notes
    for note in notes:
        if note['NoteTitle']==notename:
            note_guid = note['NoteId']
            break;
        else:
            note_guid = None
    return note_guid


client = EvernoteClient(token=auth_token, sandbox=True)
note_store = client.get_note_store()

nbs = list_notebooks(note_store)

#print note['haha']
note_guid = get_guid_from_notename(nbs, 'haha')

note_content = get_note_content(note_guid, note_store)
print '-----  target content ----------'
print note_content
print 'content ------------------------'
print note_content.content
#remain 
#?xml version="1.0" encoding="UTF-8"?>
#<!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd">
#<en-note><div>testtest</div><div>lalala for you!!!!</div></en-note>

#notebooks = note_store.listNotebooks()
#for n in notebooks:
#    print n.guid, n.name
#print notebooks

#list_notes(, 'haha', note_store)

"""
note_filter = NoteStore.NoteFilter()
note_filter.words = 'intitle:"test"'
notes_metadata_result_spec = NoteStore.NotesMetadataResultSpec()

notes_metadata_list = note_store.findNotesMetadata(note_filter, 0, 1, notes_metadata_result_spec)
print '-------notes meta data list -----------'
print notes_metadata_list
print notes_metadata_list.totalNotes
print '-----------------------------'
print notes_metadata_list.notes
for i in range(notes_metadata_list.totalNotes):
    print i
    note_guid = notes_metadata_list.notes[i].guid
    print note_guid
    note = note_store.getNote(note_guid, True, False, False, False)
    print note
"""
