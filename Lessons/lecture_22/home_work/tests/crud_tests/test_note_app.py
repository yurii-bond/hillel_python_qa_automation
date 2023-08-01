
def test_create_note(notes_app):
    assert notes_app.add_note('My first note') == "Note added successfully"


def test_read_note(notes_app):
    notes_app.add_note("My first note")
    notes_app.add_note('My second note')
    assert notes_app.get_note(0) == 'My first note'
    assert notes_app.get_note(1) == 'My second note'
    assert notes_app.get_note(2) == 'Index out of range'


def test_update_note(notes_app):
    notes_app.add_note('My first note')
    assert notes_app.edit_note(0, 'Updated note') == 'Note edited successfully'
    assert notes_app.get_note(0) == 'Updated note'


def test_delete_note(notes_app):
    notes_app.add_note('My first note')
    notes_app.add_note('My second note')
    assert notes_app.delete_note(1) == 'Note deleted successfully'
    assert notes_app.get_note(1) == 'Index out of range'
