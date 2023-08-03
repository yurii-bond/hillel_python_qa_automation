import pytest

from .....lecture_22.home_work.app.notes_app import NotesApp

def test_add_note_index_error(_NotesApp):
    _NotesApp.add_note('hi')
    result = _NotesApp.get_note(1)
    assert result == "Index out of range"

def test_get_note_index_error(_NotesApp):
    result = _NotesApp.get_note(0)
    assert result == "Index out of range"

def test_edit_note_index_error(_NotesApp):
    result = _NotesApp.edit_note(0, "Test note 1 edited")
    assert result == "Index out of range"

def test_delete_note_error(_NotesApp):
    result = _NotesApp.delete_note(1)
    assert result == "Index out of range"