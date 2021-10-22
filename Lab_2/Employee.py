from Project import Project
from Task import Task
import random
from abc import ABC, abstractmethod
from PersonalInfo import PersonalInfo
from Assignment import Assignment


class Employee(ABC):
    def __init__(self, personal_info: PersonalInfo):
        self.personal_info = personal_info
        self.assignments = []

    @property
    def personal_info(self):
        return self._personal_info

    @personal_info.setter
    def personal_info(self, personal_info):
        if isinstance(personal_info, PersonalInfo):
            self._personal_info = personal_info
        else:
            raise AttributeError("Err")

    
    def assign_possibility(self, project: Project) -> bool:
        if len(project.developers) == 0:
            print('You can add developer, nobody working here')
            return True
        else:
            print(f'You can`t add developer, {project.developers[0]} already working there')
            return False

    def assigned_projects(self, developer) -> list[Project]:
        print(f'Assigned project: {self.assignments[0]}')
        projects = []
        for assignment in self.assignments:
            projects.append(assignment.project)
        return projects

    def assign(self, project: Project) -> None:
        project.developers.append(self)
        assignment = Assignment(title=project.title, project=project)
        self.assignments.append(assignment)
        print(f"Assignment for {self.personal_info.name} to project {project.title} has been created.")

    def unassign(self, project_title: str) -> None:
        idx = -1
        for i, assignment in enumerate(self.assignments):
            if assignment.project.title == project_title:
                idx = i
                break
            if idx != -1:
                del self.assignments[idx]

    def set_task(self, task: Task):
        return task

