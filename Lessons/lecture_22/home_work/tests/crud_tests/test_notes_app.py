
def test_add_note(notes_app):
    assert notes_app.add_note("My first note") == "Note added successfully"
    assert notes_app.get_note(0) == "My first note"


def test_get_note(with_notes_app):
    assert with_notes_app.get_note(0) == "First note"


def test_edit_note(with_notes_app):
    assert with_notes_app.edit_note(0, "New note") == "Note edited successfully"
    assert with_notes_app.get_note(0) == "New note"

def test_delete_note(with_notes_app):
    assert with_notes_app.delete_note(0) == "Note deleted successfully"