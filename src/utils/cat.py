import random
import uuid


class Cat:
    id = ""
    sex = ""
    age = 0
    neutered = False
    city_area = ""
    colony_member = False
    colony_caregiver = False
    mother = ""
    father = ""
    incest = False
    dead = False
    cause_of_death = ""
    pregnant = False
    father_of_litter = ""

    def __init__(self, area: str) -> None:
        self.city_area = area
        self.id = uuid.uuid4()
        sexes = ["male", "female"]
        self.sex = random.choice(sexes)

    def age_cat(self) -> None:
        self.age += 1

    def birth(self, cats: list) -> None:
        pass

    def describe_cat(self) -> None:
        print(f'id: {self.id}')
        print(f'sex: {self.sex}')
        print(f'neutered?: {self.neutered}')
        print(f'city_area: {self.city_area}')
        print(f'Colony Member?: {self.colony_member}')
        print(f'Dead?: {self.dead}')
        print("")

    def impregnate(self, father: str) -> None:
        if not self.neutered and self.sex == "female" and self.age > 2:
            self.pregnant = True
            self.father_of_litter = father

    def mortality(self) -> None:
        pass
