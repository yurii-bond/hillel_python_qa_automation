import pytest

from Lessons.lecture_22.home_work.app.notes_app import NotesApp


@pytest.fixture
def app_without_notes():
    app = NotesApp()
    return app


@pytest.fixture
def app_with_notes():
    app = NotesApp()
    app.add_note('Test note 1')
    app.add_note('Test note 2')
    return app


@pytest.fixture
def app_get_notes():
    app = NotesApp()
    app.get_note(1)
    return app


@pytest.fixture
def app_edit_notes():
    app = NotesApp()
    app.edit_note(2, 'Edited content')
    return app