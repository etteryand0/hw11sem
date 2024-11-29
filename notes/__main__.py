from . import NoteManager


def main():
    manager = NoteManager()

    while True:
        print("Добро пожаловать в NoteManager!")
        print("Выберите действие:")
        print("1. Создать заметку")
        print("2. Просмотреть все заметки")
        print("3. Просмотреть детали заметки")
        print("4. Редактировать заметку")
        print("5. Удалить заметку")
        print("6. Импортировать заметки из CSV")
        print("7. Экспортировать заметки в CSV")
        print("8. Выход")

        choice = input("Введите номер действия: ")

        if choice == "1":
            title = input("Введите заголовок заметки: ")
            content = input("Введите содержимое заметки: ")
            manager.create_note(title, content)
            print("Заметка создана.")

        elif choice == "2":
            print("Список заметок:")
            for note in manager.notes:
                print(f"{note.id}: {note.title} - {note.timestamp}")

        elif choice == "3":
            note_id = int(input("Введите ID заметки для просмотра: "))
            manager.view_note_details(note_id)

        elif choice == "4":
            note_id = int(input("Введите ID заметки для редактирования: "))
            title = input("Введите новый заголовок (или оставьте пустым): ")
            content = input("Введите новое содержимое (или оставьте пустым): ")
            manager.edit_note(
                note_id, title if title else None, content if content else None
            )
            print("Заметка отредактирована.")

        elif choice == "5":
            note_id = int(input("Введите ID заметки для удаления: "))
            manager.delete_note(note_id)
            print("Заметка удалена.")

        elif choice == "6":
            csv_filename = input("Введите имя CSV файла для импорта: ")
            manager.import_notes(csv_filename)
            print("Заметки импортированы.")

        elif choice == "7":
            csv_filename = input("Введите имя CSV файла для экспорта: ")
            manager.export_notes(csv_filename)
            print("Заметки экспортированы.")

        elif choice == "8":
            break

        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")


if __name__ == "__main__":
    main()
