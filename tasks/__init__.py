import json
import csv


class Task:
    def __init__(
        self,
        task_id,
        title,
        description="",
        done=False,
        priority="Низкий",
        due_date=None,
    ):
        self.id = task_id
        self.title = title
        self.description = description
        self.done = done
        self.priority = priority
        self.due_date = due_date

    def to_dict(self):
        return self.__dict__


class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                tasks_data = json.load(file)
                return [Task(**task) for task in tasks_data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_tasks(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(
                [task.to_dict() for task in self.tasks],
                file,
                indent=4,
                ensure_ascii=False,
            )

    def add_task(
        self, title, description="", priority="Низкий", due_date=None, done=False
    ):
        task_id = len(self.tasks) + 1
        new_task = Task(
            task_id, title, description, priority=priority, due_date=due_date, done=done
        )
        self.tasks.append(new_task)
        self.save_tasks()

    def view_tasks(self, done=None, priority=None, due_date=None):
        for task in self.filter_tasks(done, priority, due_date):
            status = "Выполнена" if task.done else "Не выполнена"
            print(
                f"ID: {task.id}, Заголовок: {task.title}, Статус: {status}, Приоритет: {task.priority}, Срок: {task.due_date}"
            )

    def mark_task_done(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.done = True
                self.save_tasks()
                return task
        return None

    def edit_task(
        self, task_id, title=None, description=None, priority=None, due_date=None
    ):
        for task in self.tasks:
            if task.id == task_id:
                if title is not None:
                    task.title = title
                if description is not None:
                    task.description = description
                if priority is not None:
                    task.priority = priority
                if due_date is not None:
                    task.due_date = due_date
                self.save_tasks()
                return task
        return None

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.id != task_id]
        self.save_tasks()

    def import_tasks(self, csv_filename):
        with open(csv_filename, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.add_task(
                    row.get("title"),
                    row.get("description"),
                    row.get("priority"),
                    row.get("due_date"),
                    row.get("done"),
                )

    def export_tasks(self, csv_filename="tasks.csv"):
        with open(csv_filename, "w", newline="", encoding="utf-8") as file:
            fieldnames = ["id", "title", "description", "done", "priority", "due_date"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for task in self.tasks:
                writer.writerow(task.to_dict())

    def filter_tasks(self, done=None, priority=None, due_date=None):
        filtered_tasks = self.tasks
        if done is not None:
            filtered_tasks = [task for task in filtered_tasks if task.done == done]
        if priority is not None:
            filtered_tasks = [
                task for task in filtered_tasks if task.priority == priority
            ]
        if due_date is not None:
            filtered_tasks = [
                task for task in filtered_tasks if task.due_date == due_date
            ]

        return filtered_tasks


__all__ = ["Task", "TaskManager"]
