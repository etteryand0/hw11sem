import unittest
import os
import csv
from notes import NoteManager


class TestNoteManager(unittest.TestCase):
    def setUp(self):
        self.test_filename = "test_notes.json"
        self.test_csvfilename = "test_notes_export.csv"
        self.test_importfile = "test_notes_import.csv"
        self.manager = NoteManager(self.test_filename)

    def tearDown(self):
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)
        if os.path.exists(self.test_csvfilename):
            os.remove(self.test_csvfilename)
        if os.path.exists(self.test_importfile):
            os.remove(self.test_importfile)

    def test_create_note(self):
        self.manager.create_note("Test Note", "This is a test note.")
        self.assertEqual(len(self.manager.notes), 1)
        self.assertEqual(self.manager.notes[0].title, "Test Note")

    def test_edit_note(self):
        self.manager.create_note("Test Note", "This is a test note.")
        self.manager.edit_note(
            1, title="Updated Note", content="This is an updated note."
        )
        self.assertEqual(self.manager.notes[0].title, "Updated Note")
        self.assertEqual(self.manager.notes[0].content, "This is an updated note.")

    def test_delete_note(self):
        self.manager.create_note("Test Note", "This is a test note.")
        self.manager.delete_note(1)
        self.assertEqual(len(self.manager.notes), 0)

    def test_import_notes(self):
        csv_data = "title,content\nTest Note,This is a test note.\nAnother Note,This is another test note.\n"
        with open(self.test_importfile, "w", newline="", encoding="utf-8") as f:
            f.write(csv_data)

        self.manager.import_notes(self.test_importfile)
        self.assertEqual(len(self.manager.notes), 2)
        self.assertEqual(self.manager.notes[0].title, "Test Note")
        self.assertEqual(self.manager.notes[1].title, "Another Note")

    def test_export_notes(self):
        self.manager.create_note("Test Note", "This is a test note.")
        self.manager.export_notes(self.test_csvfilename)

        with open(self.test_csvfilename, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            notes = list(reader)

        self.assertEqual(len(notes), 1)
        self.assertEqual(notes[0]["title"], "Test Note")
        self.assertEqual(notes[0]["content"], "This is a test note.")


if __name__ == "__main__":
    unittest.main()
