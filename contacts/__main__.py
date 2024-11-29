from . import ContactManager


def main():
    manager = ContactManager()

    while True:
        print("\nМенеджер контактов:")
        print("1. Добавить контакт")
        print("2. Поиск контакта")
        print("3. Редактировать контакт")
        print("4. Удалить контакт")
        print("5. Экспорт контактов")
        print("6. Импорт контактов")
        print("7. Выход")

        choice = input("Выберите действие (1-7): ")

        if choice == "1":
            name = input("Введите имя контакта: ")
            phone = input("Введите номер телефона (или оставьте пустым): ")
            email = input("Введите адрес электронной почты (или оставьте пустым): ")
            manager.add_contact(name, phone, email)
            print("Контакт добавлен.")

        elif choice == "2":
            query = input("Введите имя или номер телефона для поиска: ")
            results = manager.search_contact(query)
            if results:
                print("Найденные контакты:")
                for contact in results:
                    print(
                        f"ID: {contact.id}, Имя: {contact.name}, Телефон: {contact.phone}, Email: {contact.email}"
                    )
            else:
                print("Контакты не найдены.")

        elif choice == "3":
            contact_id = int(input("Введите ID контакта для редактирования: "))
            name = input("Введите новое имя (или оставьте пустым): ")
            phone = input("Введите новый номер телефона (или оставьте пустым): ")
            email = input(
                "Введите новый адрес электронной почты (или оставьте пустым): "
            )
            updated_contact = manager.edit_contact(
                contact_id, name or None, phone or None, email or None
            )
            if updated_contact:
                print("Контакт обновлен.")
            else:
                print("Контакт не найден.")

        elif choice == "4":
            contact_id = int(input("Введите ID контакта для удаления: "))
            manager.delete_contact(contact_id)
            print("Контакт удален.")

        elif choice == "5":
            csv_filename = (
                input("Введите имя файла для экспорта [contacts.csv]: ")
                or "contacts.csv"
            )
            manager.export_contacts(csv_filename)
            print(f"Контакты экспортированы в файл '{csv_filename}'.")

        elif choice == "6":
            csv_filename = input("Введите имя файла для импорта: ")
            manager.import_contacts(csv_filename)
            print(f"Контакты импортированы из файла '{csv_filename}'.")

        elif choice == "7":
            print("Выход из программы.")
            break

        else:
            print("Некорректный ввод. Пожалуйста, выберите номер действия от 1 до 7.")


if __name__ == "__main__":
    main()
