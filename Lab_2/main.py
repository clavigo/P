from Developer import Developer, ProjectManager
from Project import Project
from datetime import datetime
from PersonalInfo import PersonalInfo

if __name__ == '__main__':
    developer = Developer(PersonalInfo(id=1, name='Judy', address='Alvarez', phone='0682794238',
                            email='JAlv@n.com', position='NUB', rank='1', salary=1000))

    project = Project(title='project', start_date=datetime.now())
    developer.assign(project)

    developer.assigned_projects(developer)
    developer.unassign(project)
    developer.assign_possibility(project)

    ProjectManager.discuss_progress(developer)



