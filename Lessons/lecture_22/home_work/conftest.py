import pytest

from ...lecture_22.home_work.app.notes_app import NotesApp


@pytest.fixture(scope='function')
def _NotesApp():
    print('new object')
    return NotesApp()