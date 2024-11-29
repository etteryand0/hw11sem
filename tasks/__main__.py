from . import TaskManager


def main():
    manager = TaskManager()

    while True:
        print("Добро пожаловать в TaskManager!")
        print("Выберите действие:")
        print("1. Добавить задачу")
        print("2. Просмотреть задачи")
        print("3. Отметить задачу как выполненную")
        print("4. Редактировать задачу")
        print("5. Удалить задачу")
        print("6. Импортировать задачи из CSV")
        print("7. Экспортировать задачи в CSV")
        print("8. Выход")

        choice = input("Введите номер действия: ")

        if choice == "1":
            title = input("Введите заголовок задачи: ")
            description = input("Введите описание задачи (или оставьте пустым): ")
            priority = (
                input("Введите приоритет задачи (Низкий/Средний/Высокий): ") or "Низкий"
            )
            due_date = input(
                "Введите срок выполнения задачи (дд-мм-гггг, или оставьте пустым): "
            )
            try:
                manager.add_task(title, description, priority, due_date)
                print("Задача добавлена.")
            except ValueError:
                print("Дата введена некорректно, повторите попытку")
                continue

        elif choice == "2":
            print("Список задач:")
            manager.view_tasks()

        elif choice == "3":
            task_id = int(input("Введите ID задачи для отметки как выполненной: "))
            task = manager.mark_task_done(task_id)
            if task:
                print(f"Задача '{task.title}' отмечена как выполненная.")
            else:
                print("Задача не найдена.")

        elif choice == "4":
            task_id = int(input("Введите ID задачи для редактирования: "))
            title = input("Введите новый заголовок (или оставьте пустым): ")
            description = input("Введите новое описание (или оставьте пустым): ")
            priority = input("Введите новый приоритет (или оставьте пустым): ")
            due_date = input("Введите новый срок (или оставьте пустым): ")
            if manager.edit_task(
                task_id,
                title if title else None,
                description if description else None,
                priority if priority else None,
                due_date if due_date else None,
            ):
                print("Задача отредактирована.")
            else:
                print("Задача не найдена.")

        elif choice == "5":
            task_id = int(input("Введите ID задачи для удаления: "))
            manager.delete_task(task_id)
            print("Задача удалена.")

        elif choice == "6":
            csv_filename = input("Введите имя CSV файла для импорта: ")
            manager.import_tasks(csv_filename)
            print("Задачи импортированы.")

        elif choice == "7":
            csv_filename = input("Введите имя CSV файла для экспорта: ")
            manager.export_tasks(csv_filename)
            print("Задачи экспортированы.")

        elif choice == "8":
            break

        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")


if __name__ == "__main__":
    main()
