import json
import csv


class Contact:
    def __init__(self, id, name, phone=None, email=None):
        self.id = id
        self.name = name
        self.phone = phone
        self.email = email

    def to_dict(self):
        return self.__dict__


class ContactManager:
    def __init__(self, filename="contacts.json"):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                contacts_data = json.load(file)
                return [Contact(**data) for data in contacts_data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_contacts(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(
                [contact.to_dict() for contact in self.contacts],
                file,
                indent=4,
                ensure_ascii=False,
            )

    def add_contact(self, name, phone=None, email=None):
        contact_id = len(self.contacts) + 1
        contact = Contact(contact_id, name, phone, email)
        self.contacts.append(contact)
        self.save_contacts()

    def search_contact(self, query):
        results = [
            contact
            for contact in self.contacts
            if query.lower() in contact.name.lower()
            or (contact.phone and query in contact.phone)
        ]
        return results

    def edit_contact(self, contact_id, name=None, phone=None, email=None):
        for contact in self.contacts:
            if contact.id == contact_id:
                if name is not None:
                    contact.name = name
                if phone is not None:
                    contact.phone = phone
                if email is not None:
                    contact.email = email
                self.save_contacts()
                return contact
        return None

    def delete_contact(self, contact_id):
        self.contacts = [
            contact for contact in self.contacts if contact.id != contact_id
        ]
        self.save_contacts()

    def import_contacts(self, csv_filename):
        with open(csv_filename, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.add_contact(row.get("name"), row.get("phone"), row.get("email"))

    def export_contacts(self, csv_filename="contacts.csv"):
        with open(csv_filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["name", "phone", "email"])
            writer.writeheader()
            for contact in self.contacts:
                writer.writerow(
                    {
                        "name": contact.name,
                        "phone": contact.phone,
                        "email": contact.email,
                    }
                )
