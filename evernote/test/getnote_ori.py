import evernote.edam.type.ttypes as Types
import evernote.edam.notestore.ttypes as NoteStore

from evernote.api.client import EvernoteClient

auth_token = "S=s1:U=8eed8:E=14e51eeb245:C=146fa3d8410:P=1cd:A=en-devtoken:V=2:H=0daa91a172de827575a961a42c4d20b4"

client = EvernoteClient(token=auth_token, sandbox=True)
note_store = client.get_note_store()

note_filter = NoteStore.NoteFilter()
note_filter.words = 'intitle:"haha"'
notes_metadata_result_spec = NoteStore.NotesMetadataResultSpec()

notes_metadata_list = note_store.findNotesMetadata(note_filter, 0, 1, notes_metadata_result_spec)

note_guid = notes_metadata_list.notes[0].guid
note = note_store.getNote(note_guid, True, False, False, False)
print note
