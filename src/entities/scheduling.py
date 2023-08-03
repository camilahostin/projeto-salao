import datetime
from entities.person import Person
from entities.service import Service

class Scheduling:

    def __init__(self, datetime_: datetime, person: Person, service: Service) -> None:
        self.datetime_ = datetime_
        self.person = person
        self.service = service
