import unittest
import os
import csv

from finance import FinanceManager


class TestFinanceManager(unittest.TestCase):
    def setUp(self):
        self.test_filename = "test_finance.json"
        self.test_importfile = "test_fin_import.csv"
        self.test_exportfile = "test_fin_export.csv"
        self.manager = FinanceManager(self.test_filename)

    def tearDown(self):
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)
        if os.path.exists(self.test_importfile):
            os.remove(self.test_importfile)
        if os.path.exists(self.test_exportfile):
            os.remove(self.test_exportfile)

    def test_add_record(self):
        self.manager.add_record(
            1500.00, "Зарплата", "01-10-2023", "Зарплата за сентябрь"
        )
        self.assertEqual(len(self.manager.records), 1)
        self.assertEqual(self.manager.records[0].amount, 1500.00)

    def test_view_records(self):
        self.manager.add_record(
            1500.00, "Зарплата", "01-10-2023", "Зарплата за сентябрь"
        )
        self.manager.add_record(-200.00, "Еда", "05-10-2023", "Покупка продуктов")
        results = self.manager.view_records(category="Еда")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].description, "Покупка продуктов")

    def test_generate_report(self):
        self.manager.add_record(
            1500.00, "Зарплата", "01-10-2023", "Зарплата за сентябрь"
        )
        self.manager.add_record(-200.00, "Еда", "05-10-2023", "Покупка продуктов")
        report = self.manager.generate_report("01-10-2023", "31-10-2023")
        self.assertEqual(len(report), 2)  # Должны быть 2 записи в отчете

    def test_calculate_balance(self):
        self.manager.add_record(
            1500.00, "Зарплата", "01-10-2023", "Зарплата за сентябрь"
        )
        self.manager.add_record(-200.00, "Еда", "05-10-2023", "Покупка продуктов")
        balance = self.manager.calculate_balance()
        self.assertEqual(balance, 1300.00)

    def test_import_records(self):
        csv_data = "amount,category,date,description\n1500.00,Зарплата,01-10-2023,Зарплата за сентябрь\n-200.00,Еда,05-10-2023,Покупка продуктов\n"
        with open(self.test_importfile, "w", newline="", encoding="utf-8") as f:
            f.write(csv_data)

        self.manager.import_records(self.test_importfile)
        self.assertEqual(len(self.manager.records), 2)
        self.assertEqual(self.manager.records[0].description, "Зарплата за сентябрь")

    def test_export_records(self):
        self.manager.add_record(
            1500.00, "Зарплата", "01-10-2023", "Зарплата за сентябрь"
        )
        self.manager.export_records(self.test_exportfile)

        with open(self.test_exportfile, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            records = list(reader)

        self.assertEqual(len(records), 1)
        self.assertEqual(float(records[0]["amount"]), 1500.00)
        self.assertEqual(records[0]["category"], "Зарплата")
        self.assertEqual(records[0]["description"], "Зарплата за сентябрь")


if __name__ == "__main__":
    unittest.main()
