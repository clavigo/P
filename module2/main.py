from abc import ABCMeta, abstractmethod, ABC
import string
import random
from dataclasses import dataclass


@dataclass
class PersonalInfo:
    id: int
    name: str
    address: str
    phone_number: str
    email: str
    position: int
    rank: str
    salary: float
    team_id: int = -1


class Member(metaclass=ABCMeta):
    def __init__(self, id: int, software):
        self.id = id
        self.software = software

    def attach_member(self):
        print(f"Member with id={self.id} is attached")
        self.software.members.append(self.id)

    def detach_member(self):
        print(f"Member with id={self.id} id detached")
        self.software.members.remove(self.id)

    @abstractmethod
    def work_with_software(self):
        pass


class Developer(Member):
    def __init__(self, id, software):
        super(Developer, self).__init__(id, software)

    def work_with_software(self):
        self.attach_member()

        self.software.create_request(self.id)
        self.software.add_features()
        self.detach_member()


class SoftwareArchitect(Member):
    def __init__(self, id, software):
        super(SoftwareArchitect, self).__init__(id, software)

    def work_with_software(self):
        self.attach_member()

        self.software.create_request(self.id)
        self.software.add_features()
        self.detach_member()


class TeamLead(Member):
    def __init__(self, id, software):
        super(TeamLead, self).__init__(id, software)

    def work_with_software(self):
        self.attach_member()
        print(f"{self.__class__.__name__} with id={self.id} is working")

        self.software.create_request(self.id, )
        self.software.add_features()
        self.detach_member()


class QA(Member):
    def __init__(self, id, software):
        super(QA, self).__init__(id, software)

    def work_with_software(self):
        self.attach_member()
        self.software.create_request(self.id)
        self.software.add_features()
        self.detach_member()


class BusinessAnalyst(Member):
    def __init__(self, id, software):
        super(BusinessAnalyst, self).__init__(id, software)

    def work_with_software(self):
        self.attach_member()
        print(f"{self.__class__.__name__} with id={self.id} is working")

        self.software.create_request(self.id)
        self.software.add_features()
        self.detach_member()


class Software(metaclass=ABCMeta):
    def __init__(self, id: int):
        self.id = id
        self.api = {}
        self.members = []
        self._password = self.get_secure_password(16)

    def _check_member(self, member_id):
        if member_id in self.members:
            print(f'Member with id={member_id} is available')
            return True
        else:
            return False

    @staticmethod
    def get_secure_password(length: int):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(length))
        return password

    @abstractmethod
    def create_request(self, member_id):
        pass

    @abstractmethod
    def __str__(self):
        pass


class MobileApp(Software):
    def __init__(self, id):
        super(MobileApp, self).__init__(id)

    @abstractmethod
    def add_features(self):
        pass


class Android(MobileApp):
    def __init__(self, id, android: str = 'ANDROID'):
        super(MobileApp, self).__init__(id)
        self.android = android


class IOS(MobileApp):
    def __init__(self, id, ios: str = 'IOS'):
        super(MobileApp, self).__init__(id)
        self.ios = ios


class WebApp(Software):
    def __init__(self, id):
        super(WebApp, self).__init__(id)

    def create_request(self, member_id: int):
        print('Web App request.')

    def __str__(self):
        return f"WebApp[id={self.id}], API[PASSWORD]={self._password}"

    @abstractmethod
    def add_features(self):
        pass


class JSBackend(WebApp):
    def __init__(self, id, js: str = 'JS'):
        super(WebApp, self).__init__(id)
        self.js = js


class PythonBackend(WebApp):
    def __init__(self, id, python: str = 'PYTHON'):
        super(WebApp, self).__init__(id)
        self.python = python


class JSFrontend(WebApp):
    def __init__(self, id, html: str = 'HTML', css: str = 'CSS', js: str = 'JS'):
        super(WebApp, self).__init__(id)
        self.html = html
        self.css = css
        self.js = js

    def connect_frontend(self):
        print(f"{self.js} is added to the Frontend")
        print(f"Frontend is connected with {self.html} and {self.css}")

    def add_features(self):
        print(f'Web App is working with {self.__class__.__name__}')
        self.connect_frontend()


class DatabaseAPI(Software, ABC):
    def __init__(self, id):
        super(DatabaseAPI, self).__init__(id)


class Containerization(Software):
    def __init__(self, id):
        super(Containerization, self).__init__(id)


class Deployment(Software):
    def __init__(self, id):
        super(Deployment, self).__init__(id)


software = JSFrontend(id=1)

developer = Developer(id=1, software=software)

print()

qa = QA(id=2, software=software)
qa.work_with_software()
