import datetime
from src.entities.person import Person
from src.entities.service import Service

class Scheduling:

    def __init__(self, datetime_: datetime, person: Person, service: Service) -> None:
        self.datetime_ = datetime_
        self.person = person
        self.service = service
