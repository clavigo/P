from datetime import datetime


class Project:
    def __init__(self, title: str, start_date: datetime) -> None:
        self.title = title
        self.start_date = start_date
        self.task_list = []
        self.developers = []
        self.qa = []
        self.project_manager = []

    def add_developer(self, developer_id) -> None:
        self.developers.append(developer_id)

    def remove_developer(self, developer_id) -> None:
        self.developers.remove(developer_id)
