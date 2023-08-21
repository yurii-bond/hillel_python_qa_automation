import pytest
from app.notes_app import Note, NotesApp

@pytest.fixture
def notes_app():
    app = NotesApp()
    return app

@pytest.fixture(scope="function")
def with_notes_app():
    app = NotesApp()
    app.add_note("First note")
    return app