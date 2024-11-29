import unittest
import os
import csv
from tasks import TaskManager


class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.test_filename = "test_tasks.json"
        self.test_csvfilename = "test_tasks_export.csv"
        self.test_importfile = "test_tasks_import.csv"
        self.manager = TaskManager(self.test_filename)

    def tearDown(self):
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)
        if os.path.exists(self.test_csvfilename):
            os.remove(self.test_csvfilename)
        if os.path.exists(self.test_importfile):
            os.remove(self.test_importfile)

    def test_add_task(self):
        self.manager.add_task(
            "Test Task", "This is a test task.", "Низкий", "01-01-2023"
        )
        self.assertEqual(len(self.manager.tasks), 1)
        self.assertEqual(self.manager.tasks[0].title, "Test Task")

    def test_edit_task(self):
        self.manager.add_task("Test Task", "This is a test task.")
        self.manager.edit_task(
            1,
            title="Updated Task",
            description="Updated description",
            priority="Высокий",
            due_date="02-02-2023",
        )
        self.assertEqual(self.manager.tasks[0].title, "Updated Task")
        self.assertEqual(self.manager.tasks[0].description, "Updated description")
        self.assertEqual(self.manager.tasks[0].priority, "Высокий")
        self.assertEqual(self.manager.tasks[0].due_date, "02-02-2023")

    def test_delete_task(self):
        self.manager.add_task("Test Task", "This is a test task.")
        self.manager.delete_task(1)
        self.assertEqual(len(self.manager.tasks), 0)

    def test_import_tasks(self):
        csv_data = "title,description,priority,due_date,done\nTest Task,This is a test task.,Низкий,01-01-2023,False\nAnother Task,This is another task.,Средний,02-02-2023,False\n"
        with open(self.test_importfile, "w", newline="", encoding="utf-8") as f:
            f.write(csv_data)

        self.manager.import_tasks(self.test_importfile)
        self.assertEqual(len(self.manager.tasks), 2)
        self.assertEqual(self.manager.tasks[0].title, "Test Task")
        self.assertEqual(self.manager.tasks[1].title, "Another Task")

    def test_export_tasks(self):
        self.manager.add_task("Test Task", "This is a test task.")
        self.manager.export_tasks(self.test_csvfilename)

        with open(self.test_csvfilename, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            tasks = list(reader)

        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["title"], "Test Task")
        self.assertEqual(tasks[0]["description"], "This is a test task.")
        self.assertEqual(tasks[0]["priority"], "Низкий")


if __name__ == "__main__":
    unittest.main()
