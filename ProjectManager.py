from Developer import Developer
from Project import Project
import random

class ProjectManager:
    def __init__(self, id: int, first_name: str, last_name: str, address: str, phone_number: str, email: str,
                 salary: float, project: Project):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.salary = salary
        self.project = project

    def discuss_progress(developer: Developer):
        progress_list = ['good job', 'bad work, fix this', 'this is awful, remake it all']
        print(f'Oh, {developer.last_name},',random.choice(progress_list))
