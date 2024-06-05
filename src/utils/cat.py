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

    def __init__(self, area: str) -> None:
        self.city_area = area
        self.id = uuid.uuid4()
        sexes = ["male", "female"]
        self.sex = random.choice(sexes)

    def describe_cat(self) -> None:
        print(f'id: {self.id}')
        print(f'sex: {self.sex}')
        print(f'neutered?: {self.neutered}')
        print(f'city_area: {self.city_area}')
        print(f'Colony Member?: {self.colony_member}')
        print(f'Dead?: {self.dead}')
        print("")
