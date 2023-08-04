def test_add_note_one(app_without_notes):
    result = app_without_notes.add_note('Test note 1')
    assert result == "Note added successfully"
    assert len(app_without_notes.notes_list) == 1
    assert app_without_notes.notes_list[0].content == "Test note 1"


def test_add_note_test_two(app_without_notes):
    result = app_without_notes.add_note('Test note 2')
    assert result == "Note added successfully"
    assert len(app_without_notes.notes_list) == 1
    assert app_without_notes.notes_list[0].content == "Test note 2"


def test_add_note_test_three(app_without_notes):
    result = app_without_notes.add_note('Test note 3')
    assert result == "Note added successfully"
    assert len(app_without_notes.notes_list) == 1
    assert app_without_notes.notes_list[0].content == "Test note 3"


def test_get_note_one(app_with_notes):
    result = app_with_notes.get_note(0)
    assert result == "Test note 1"


def test_get_note_two(app_with_notes):
    result = app_with_notes.get_note(1)
    assert result == "Test note 2"


def test_edit_note_one(app_with_notes):
    app_with_notes.edit_note(0, "Test note 1 edited")
    result = app_with_notes.get_note(0)
    assert result == "Test note 1 edited"


def test_edit_note_two(app_with_notes):
    app_with_notes.edit_note(1, 'Test note 2 edited')
    result = app_with_notes.get_note(1)
    assert result == "Test note 2 edited"


def test_delete_note_one(app_with_notes):
    result = app_with_notes.delete_note(1)
    assert result == 'Note deleted successfully'
    assert len(app_with_notes.notes_list) == 1
