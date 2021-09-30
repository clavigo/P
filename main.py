from Project import Project
from datetime import datetime
from ProjectManager import ProjectManager
from Developer import Developer

if __name__ == '__main__':
    developer = Developer(id=1, first_name='test', last_name='test', address='test',
                          phone_number='123654789', email='test@test.test', position='junior', rank=2, salary=500)
    project = Project(title='project', start_date=datetime.now())
    developer.assign(project)
