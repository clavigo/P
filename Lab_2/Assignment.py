from datetime import datetime
from collections import defaultdict


class Assignment:
    def __init__(self, title: str, project):
        self.title = title
        self.project = project
        self.received_tasks = defaultdict(list)

    def get_tasks_by_date(self, date_by: datetime) -> list:
        task_by_date = []
        for date, tasks in self.received_tasks.items():
            if date <= date_by:
                task_by_date.append(tasks)

        return task_by_date

    def add_task(self, task):
        self.received_tasks[datetime.now()].append(task)


