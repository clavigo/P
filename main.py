from Project import Project
from datetime import datetime
from ProjectManager import ProjectManager
from Developer import Developer

if __name__ == '__main__':
    developer = Developer(id=1, first_name='Judy', last_name='Alvarez', address='NightCity',
                          phone_number='682794238', email='JAlv@n.com', position='NUB', rank=1, salary=1000)
    project = Project(title='project', start_date=datetime.now())
    developer.assign(project)

    developer.assigned_projects(developer)
    developer.assign_possibility(project)
    developer.unassign(project)
    developer.assign_possibility(project)


    ProjectManager.discuss_progress(developer)
    
    
    #project.add_developer('test')
    #for x in project.developers: print(x)
    #project.remove_developer('test')
    #for x in project.developers: print(x)