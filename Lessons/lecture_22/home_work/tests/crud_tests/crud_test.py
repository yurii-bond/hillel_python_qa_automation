import pytest
from app.notes_app import NotesApp

@pytest.fixture
def notes_app_instance():
    return NotesApp()

def test_add_note(notes_app_instance):
    result = notes_app_instance.add_note("New note content")
    assert result == "Note added successfully"
    assert len(notes_app_instance.notes_list) == 1

def test_get_note(notes_app_instance):
    notes_app_instance.add_note("Test note")
    result = notes_app_instance.get_note(0)
    assert result == "Test note"

def test_edit_note(notes_app_instance):
    notes_app_instance.add_note("Test note")
    notes_app_instance.edit_note(0, "Edited note")
    result = notes_app_instance.get_note(0)
    assert result == "Edited note"

def test_delete_note(notes_app_instance):
    notes_app_instance.add_note("Test note")
    notes_app_instance.delete_note(0)
    assert len(notes_app_instance.notes_list) == 0
