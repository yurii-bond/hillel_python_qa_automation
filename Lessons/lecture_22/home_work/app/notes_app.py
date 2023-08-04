def delete_note(self, index):
     try:
         del self.notes_list[index]
         return "Note deleted successfully"
     except IndexError:
         return "Index out of range"
