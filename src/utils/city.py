import random
from . import cat


def find_cats_in_area(cats: list, area_id: str) -> list:
    boys = []
    girls = []
    for kitty in cats:
        if kitty.city_area == area_id and kitty.sex == "male":
            boys.append(kitty)
        elif kitty.city_area == area_id and kitty.sex == "female":
            girls.append(kitty)
    return boys, girls


class City:
    '''A Class Defining a City as a Construct'''

    def __init__(self, size=1) -> None:
        self.areas = []
        '''Divide an area, given in square kilometers
        into 1x1 kilometer areas'''
        iterator = 0
        while iterator < size:
            self.areas.append("area_" + str(iterator))
            iterator += 1
        # 365 homes, on average, in a square mile in Iowa
        self.homes = len(self.areas) * 365
        self.feeders = round(self.homes * .1)

    def age_all_cats(self, cats: list) -> None:
        for kitty in cats:
            kitty.age_cat()

    def birth_cats(self, cats: list) -> int:
        # cats give birth

        # return number of births this time slice
        pass

    def breed_cats(self, cats: list) -> None:
        for area in self.areas:
            boys, girls = find_cats_in_area(cats, area)
            while len(boys) < 0 and len(girls) < 0:
                dad = boys.pop(1)
                mom = girls.pop(1)
                mom.impregnate(dad.id)
                # one male cat will impregnante every cat he can
                boys.append(dad)

    def describe_city(self) -> None:
        print(f"City is {len(self.areas)} square kilometers")
        print(f"Homes in city: {self.homes}")
        print(f"Feeding homes: {self.feeders}")

    def migrate_cats(self, cats_area_1: list, cats_area_2: list) -> None:
        pass

    def return_random_area(self) -> str:
        return random.choice(self.areas)

    def seed_cats(self, seed_size: int, living_cats: list) -> None:
        # seed number for cats to start simulation
        # representing a number of cats abandoned by owners
        iterator = 1
        while iterator < seed_size:
            area = self.return_random_area()
            temp_cat = cat.Cat(area)
            temp_cat2 = cat.Cat(area)
            living_cats.append(temp_cat)
            living_cats.append(temp_cat2)
            iterator += 2
