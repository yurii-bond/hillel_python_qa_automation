import pytest
from app.notes_app import NotesApp

@pytest.fixture
def notes_app_instance():
    return NotesApp()

def test_add_note_index_error(notes_app_instance):
    with pytest.raises(IndexError):
        notes_app_instance.get_note(0)

def test_edit_note_index_error(notes_app_instance):
    with pytest.raises(IndexError):
        notes_app_instance.edit_note(0, "Edited note")

def test_delete_note_index_error(notes_app_instance):
    with pytest.raises(IndexError):
        notes_app_instance.delete_note(0)
