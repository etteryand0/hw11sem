import unittest
import os
import csv

from contacts import ContactManager


class TestContactManager(unittest.TestCase):
    def setUp(self):
        self.test_filename = "test_contacts.json"
        self.test_csvfilename = "test_export.csv"
        self.test_importfile = "test_import.csv"
        self.manager = ContactManager(self.test_filename)

    def tearDown(self):
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)
        if os.path.exists(self.test_csvfilename):
            os.remove(self.test_csvfilename)
        if os.path.exists(self.test_importfile):
            os.remove(self.test_importfile)

    def test_add_contact(self):
        self.manager.add_contact("Иван Иванов", "123456789", "ivan@example.com")
        self.assertEqual(len(self.manager.contacts), 1)
        self.assertEqual(self.manager.contacts[0].name, "Иван Иванов")

    def test_search_contact(self):
        self.manager.add_contact("Иван Иванов", "123456789", "ivan@example.com")
        self.manager.add_contact("Петр Петров", "987654321", "petr@example.com")
        results = self.manager.search_contact("Иван")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].name, "Иван Иванов")

    def test_edit_contact(self):
        self.manager.add_contact("Иван Иванов", "123456789", "ivan@example.com")
        self.manager.edit_contact(1, name="Иван Сидоров", phone="111222333")
        self.assertEqual(self.manager.contacts[0].name, "Иван Сидоров")
        self.assertEqual(self.manager.contacts[0].phone, "111222333")

    def test_delete_contact(self):
        self.manager.add_contact("Иван Иванов", "123456789", "ivan@example.com")
        self.manager.delete_contact(1)
        self.assertEqual(len(self.manager.contacts), 0)

    def test_import_contacts(self):
        csv_data = "name,phone,email\nИван Иванов,123456789,ivan@example.com\nПетр Петров,987654321,petr@example.com\n"
        with open(self.test_importfile, "w", newline="", encoding="utf-8") as f:
            f.write(csv_data)

        self.manager.import_contacts(self.test_importfile)
        self.assertEqual(len(self.manager.contacts), 2)
        self.assertEqual(self.manager.contacts[0].name, "Иван Иванов")
        self.assertEqual(self.manager.contacts[1].name, "Петр Петров")

        os.remove(self.test_importfile)

    def test_export_contacts(self):
        self.manager.add_contact("Иван Иванов", "123456789", "ivan@example.com")
        self.manager.export_contacts(self.test_csvfilename)

        with open(self.test_csvfilename, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            contacts = list(reader)

        self.assertEqual(len(contacts), 1)
        self.assertEqual(contacts[0]["name"], "Иван Иванов")
        self.assertEqual(contacts[0]["phone"], "123456789")
        self.assertEqual(contacts[0]["email"], "ivan@example.com")

        os.remove(self.test_csvfilename)


if __name__ == "__main__":
    unittest.main()
