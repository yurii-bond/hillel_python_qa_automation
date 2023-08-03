
def test_add_note(_NotesApp):
    result = _NotesApp.add_note("Test note 1")
    assert result == "Note added successfully"
    assert len(_NotesApp.notes_list) == 1
    assert _NotesApp.notes_list[0].content == "Test note 1"

def test_get_note(_NotesApp):
    _NotesApp.add_note("Test note 1")
    result = _NotesApp.get_note(0)
    assert result == "Test note 1"

def test_edit_note(_NotesApp):
    _NotesApp.add_note("Test note 1")
    _NotesApp.edit_note(0, "Test note 1 edited")
    result = _NotesApp.get_note(0)
    assert result == "Test note 1 edited"

def test_delete_note(_NotesApp):
    _NotesApp.add_note("Test note 1")
    _NotesApp.delete_note(0)
    assert len(_NotesApp.notes_list) == 0