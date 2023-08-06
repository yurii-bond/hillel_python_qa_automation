import pytest
from ...lecture_22.home_work.app.notes_app import NotesApp


@pytest.fixture(scope='function')
def notes_app():
    print('Fixture object created')
    return NotesApp()
