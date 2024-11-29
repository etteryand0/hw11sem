import json
import csv
from datetime import datetime


class FinanceRecord:
    def __init__(self, id, amount, category, date, description):
        self.id = id
        self.amount = amount
        self.category = category
        self.date = datetime.strptime(date, "%d-%m-%Y")
        self.description = description

    def to_dict(self):
        return {
            "id": self.id,
            "amount": self.amount,
            "category": self.category,
            "date": self.date.strftime("%d-%m-%Y"),
            "description": self.description,
        }


class FinanceManager:
    def __init__(self, filename="finance.json"):
        self.filename = filename
        self.records = self.load_records()

    def load_records(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                records_data = json.load(file)
                return [FinanceRecord(**data) for data in records_data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_records(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(
                [record.to_dict() for record in self.records],
                file,
                indent=4,
                ensure_ascii=False,
            )

    def add_record(self, amount, category, date, description):
        record_id = len(self.records) + 1
        record = FinanceRecord(record_id, amount, category, date, description)
        self.records.append(record)
        self.save_records()

    def view_records(self, category=None, date=None):
        results = self.records
        if category:
            results = [
                record
                for record in results
                if record.category.lower() == category.lower()
            ]
        if date:
            date_filter = datetime.strptime(date, "%d-%m-%Y")
            results = [
                record for record in results if record.date.date() == date_filter.date()
            ]
        return results

    def generate_report(self, start_date, end_date):
        start = datetime.strptime(start_date, "%d-%m-%Y")
        end = datetime.strptime(end_date, "%d-%m-%Y")
        report = [record for record in self.records if start <= record.date <= end]
        return report

    def calculate_balance(self):
        return sum(record.amount for record in self.records)

    def import_records(self, csv_filename):
        with open(csv_filename, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.add_record(
                    float(row["amount"]),
                    row["category"],
                    row["date"],
                    row["description"],
                )

    def export_records(self, csv_filename):
        with open(csv_filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=[
                    "id",
                    "amount",
                    "category",
                    "date",
                    "description",
                ],
            )
            writer.writeheader()
            for record in self.records:
                writer.writerow(record.to_dict())


__all__ = ["FinanceRecord", "FinanceManager"]
