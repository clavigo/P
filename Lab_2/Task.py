from datetime import datetime


class Task:
    def __init__(self, id: int, title: str, deadline: datetime,
                 status: float, related_project: str):
        self.id = id
        self.title = title
        self.deadline = deadline
        self.items = []
        self.status = status
        self.related_project = related_project
        self.comments = []

    def implement_item(self, item_name: str) -> str:
        pass

    def add_comment(self, comment: str) -> None:
        self.comments.append(comment)
