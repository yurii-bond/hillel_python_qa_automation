import pytest


def test_create_note_empty_content(empty_notes_app):
    assert empty_notes_app.add_note("") == "Note added successfully"


def test_read_note_invalid_index(empty_notes_app):
    assert empty_notes_app.get_note(0) == "Index out of range"


def test_update_note_invalid_index(empty_notes_app):
    assert empty_notes_app.edit_note(1, "Updated note") == "Index out of range"


def test_delete_note_invalid_index(empty_notes_app):
    assert empty_notes_app.delete_note(2) == "Index out of range"


def test_get_note_nonexistent_index(sample_notes_app):
    assert sample_notes_app.get_note(3) == "Index out of range"


def test_edit_note_nonexistent_index(sample_notes_app):
    assert sample_notes_app.edit_note(4, "Updated note") == "Index out of range"
