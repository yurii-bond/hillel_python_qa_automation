class Note:
    def __init__(self, content):
        self.content = content


class NotesApp:
    def __init__(self):
        self.notes_list = []

    def add_note(self, content):
        new_note = Note(content)
        self.notes_list.append(new_note)
        return "Note added successfully"

    def get_note(self, index):
        try:
            return self.notes_list[index].content
        except IndexError:
            return "Index out of range"

    def edit_note(self, index, content):
        try:
            self.notes_list[index].content = content
            return "Note edited successfully"
        except IndexError:
            return "Index out of range"

    def delete_note(self, index):
        try:
            del self.notes_list[index]
            return 'Note deleted successfully'
        except IndexError:
            return 'Index out of range'


notes_app = NotesApp()

# add note
notes_app.add_note('Test first note')
notes_app.add_note('Test second note')

# show note
print(notes_app.get_note(0))
print(notes_app.get_note(1))

# edit note
notes_app.edit_note(0, 'Edit first note')
print(notes_app.get_note(0))

# delete note
notes_app.delete_note(1)
print(notes_app.get_note(1))

