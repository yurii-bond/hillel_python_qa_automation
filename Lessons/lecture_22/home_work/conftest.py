import pytest
from Lessons.lecture_22.home_work.app.notes_app import Note, NotesApp


@pytest.fixture
def notes_app():
    app = NotesApp()
    yield app
    # app.notes_list = []


@pytest.fixture(scope='function')
def empty_notes_app():
    app = NotesApp
    return app()


@pytest.fixture(scope='function')
def sample_notes_app():
    app = NotesApp()
    app.add_note("First note")
    app.add_note("Second note")
    return app
