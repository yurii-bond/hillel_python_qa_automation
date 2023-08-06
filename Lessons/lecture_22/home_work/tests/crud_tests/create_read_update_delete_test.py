def test_add_note_success(notes_app):
    assert notes_app.add_note("Test note") == "Note added successfully"

def test_get_note_valid_index(notes_app):
    notes_app.add_note("Test note")
    assert notes_app.get_note(0) == "Test note"

def test_get_note_invalid_index(notes_app):
    assert notes_app.get_note(0) == "Index out of range"

def test_update_note_success(notes_app):
    notes_app.add_note("Test note")
    assert notes_app.edit_note(0, "Edited note") == "Note edited successfully"

def test_edit_note_invalid_index(notes_app):
    assert notes_app.edit_note(0, "Edited note") == "Index out of range"

