from . import FinanceManager


def main():
    manager = FinanceManager()

    while True:
        print("Финансовый менеджер.")
        print("Выберите действие:")
        print("1. Добавить запись")
        print("2. Просмотреть записи")
        print("3. Сгенерировать отчет")
        print("4. Рассчитать баланс")
        print("5. Импортировать записи из CSV")
        print("6. Экспортировать записи в CSV")
        print("7. Выход")

        choice = input("Введите номер действия: ")

        if choice == "1":
            try:
                amount = float(input("Введите сумму: "))
            except ValueError:
                print("Вы ввели не число")
                continue
            category = input("Введите категорию: ")
            date = input("Введите дату (дд-мм-гггг): ")
            description = input("Введите описание: ")
            try:
                manager.add_record(amount, category, date, description)
                print("Запись добавлена.")
            except ValueError:
                print("Дата введена некорректно, повторите попытку")
                continue

        elif choice == "2":
            category = input("Введите категорию (или оставьте пустым для всех): ")
            date = input("Введите дату (дд-мм-гггг) (или оставьте пустым для всех): ")

            try:
                records = manager.view_records(
                    category if category else None, date if date else None
                )
                for record in records:
                    print(record.to_dict())
            except ValueError:
                print("Дата введена некорректно, повторите попытку")
                continue

        elif choice == "3":
            start_date = input("Введите начальную дату (дд-мм-гггг): ")
            end_date = input("Введите конечную дату (дд-мм-гггг): ")

            try:
                report = manager.generate_report(start_date, end_date)
                for record in report:
                    print(record.to_dict())
            except ValueError:
                print("Дата введена некорректно, повторите попытку")
                continue

        elif choice == "4":
            balance = manager.calculate_balance()
            print(f"Текущий баланс: {balance}")

        elif choice == "5":
            csv_filename = input("Введите имя CSV файла для импорта: ")
            manager.import_records(csv_filename)
            print("Записи импортированы.")

        elif choice == "6":
            csv_filename = input("Введите имя CSV файла для экспорта: ")
            manager.export_records(csv_filename)
            print("Записи экспортированы.")

        elif choice == "7":
            break

        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")


if __name__ == "__main__":
    main()
