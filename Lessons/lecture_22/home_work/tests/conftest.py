import pytest
from app.notes_app import NotesApp

@pytest.fixture(scope="function")
def notes_app_instance():
    return NotesApp()

@pytest.fixture(scope="module")
def notes_app_module():
    return NotesApp()

@pytest.fixture(scope="session")
def notes_app_session():
    return NotesApp()


@pytest.fixture(scope="function")
def notes_app_instance():
    return NotesApp()

@pytest.fixture(scope="module")
def notes_app_module():
    return NotesApp()

@pytest.fixture(scope="session")
def notes_app_session():
    return NotesApp()
