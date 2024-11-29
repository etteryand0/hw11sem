from datetime import datetime
import json
import csv


class Note:
    def __init__(self, id, title, content):
        self.id = id
        self.title = title
        self.content = content
        self.timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    def to_dict(self):
        return self.__dict__


class NoteManager:
    def __init__(self, filename="notes.json"):
        self.filename = filename
        self.notes = self.load_notes()

    def load_notes(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                notes_data = json.load(file)
                return [Note(**note) for note in notes_data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_notes(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(
                [note.to_dict() for note in self.notes],
                file,
                indent=4,
                ensure_ascii=False,
            )

    def create_note(self, title, content):
        note_id = len(self.notes) + 1
        note = Note(note_id, title, content)
        self.notes.append(note)
        self.save_notes()

    def view_notes(self):
        for note in self.notes:
            print(f"{note.id}: {note.title} - {note.timestamp}")

    def view_note_details(self, note_id):
        for note in self.notes:
            if note.id == note_id:
                print(
                    f"Title: {note.title}\nContent: {note.content}\nTimestamp: {note.timestamp}"
                )
                return
        print("Заметка не найдена.")

    def edit_note(self, note_id, title=None, content=None):
        for note in self.notes:
            if note.id == note_id:
                if title:
                    note.title = title
                if content:
                    note.content = content
                note.timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                self.save_notes()
                return
        print("Заметка не найдена.")

    def delete_note(self, note_id):
        self.notes = [note for note in self.notes if note.id != note_id]
        self.save_notes()

    def import_notes(self, csv_filename):
        with open(csv_filename, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.create_note(row["title"], row["content"])

    def export_notes(self, csv_filename="notes.csv"):
        with open(csv_filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["title", "content"])
            writer.writeheader()
            for note in self.notes:
                writer.writerow(note.to_dict())


__all__ = ["Note", "NoteManager"]
