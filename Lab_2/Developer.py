from Employee import Employee
from PersonalInfo import PersonalInfo
from Task import Task
import random
from abc import ABC, abstractmethod

class Developer(Employee):
    def __init__(self, personal_info: PersonalInfo):
        super().__init__(personal_info=personal_info)
        self.assignments = []

    def set_task(self, task: Task):
        for assignment in self.assignments:
            if assignment.project.title == task.related_project:
                assignment.project.task_list.append(task)
#                assignment.add_task(task)

    def calculate_tax(self) -> float:
        pass

    def calculate_salary(self) -> None:
        pass


class ProjectManager(Employee):
    def __init__(self, personal_info: PersonalInfo):
        super().__init__(personal_info=personal_info)

    def calculate_tax(self) -> float:
        pass

    def calculate_salary(self) -> None:
        pass

    def discuss_progress(developer: Employee):
        progress_list = ["The job is excellent!", "Yes! Our project already done", "Congratulation, the job is nice",
         "Can you redo this work?", "Ahh shit, this job is awful"]
        print(f'Oh, {developer.personal_info.name},', random.choice(progress_list))

    @abstractmethod
    def calculate_tax(self) -> float:
        pass

    @abstractmethod
    def calculate_salary(self) -> None:
        pass


class QualityAssurance(Employee):
    def __init__(self, personal_info: PersonalInfo):
        super().__init__(personal_info=personal_info)

    def calculate_tax(self) -> float:
        pass

    def calculate_salary(self) -> None:
        pass
