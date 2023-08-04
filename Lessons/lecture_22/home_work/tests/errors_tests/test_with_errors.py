import sys

import pytest


def test_get_note_three(app_without_notes):
    result = app_without_notes.get_note(2)
    assert result == "Index out of range"


def test_get_note_four(app_with_notes):
    result = app_with_notes.get_note(3)
    assert result == "Index out of range"


def test_edit_note_three(app_with_notes):
    app_with_notes.edit_note(3, 'Test note 2 edited')
    result = app_with_notes.get_note(3)
    assert result == "Index out of range"


def test_delete_note_two(app_with_notes):
    result = app_with_notes.delete_note(2)
    assert result == 'Index out of range'
    assert len(app_with_notes.notes_list) == 2


def test_delete_note_three(app_without_notes):
    result = app_without_notes.delete_note(0)
    assert result == 'Index out of range'
    assert len(app_without_notes.notes_list) == 0