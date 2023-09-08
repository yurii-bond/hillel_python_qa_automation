def test_without_note(notes_app):
    assert notes_app.add_note("") == "Note added successfully"


def test_get_note_with_wrong_index(notes_app):
    assert notes_app.get_note(2) == "Index out of range"


def test_edit_note_wrong_index(with_notes_app):
    assert with_notes_app.edit_note(5, "New note") == "Index out of range"


def test_delete_note(with_notes_app):
    assert with_notes_app.delete_note(2) == "Index out of range"
