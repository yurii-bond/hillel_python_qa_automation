def test_add_note_empty_content(notes_app):
    assert notes_app.add_note("") == "Note added successfully"

def test_get_note_negative_index(notes_app):
    assert notes_app.get_note(-1) == "Index out of range"

def test_edit_note_negative_index(notes_app):
    assert notes_app.edit_note(-1, "Edited note") == "Index out of range"

def test_edit_note_invalid_index(notes_app):
    assert notes_app.edit_note(0, "Edited note") == "Index out of range"
