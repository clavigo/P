from dataclasses import dataclass


@dataclass
class PersonalInfo:
    id: int
    name: str
    address: str
    phone: str
    email: str
    position: int
    rank: str
    salary: float

