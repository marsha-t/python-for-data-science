import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Represent a student with generated login and ID"""
    name: str
    surname: str # TODO what if surname not given fully in lowercase
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False, default_factory=generate_id)

    def __post_init__(self) -> None:
        """Create student login after initialisation"""
        self.login = self.name[0].upper() + self.surname.lower()
