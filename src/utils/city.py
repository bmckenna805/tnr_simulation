import random
from . import cat


class City:
    '''A Class Defining a City as a Construct'''
    areas = []

    def __init__(self, size: int) -> None:
        '''Divide an area, given in square kilometers
        into 1x1 kilometer areas'''
        iterator = 1
        while iterator < size:
            self.areas.append("area_" + str(iterator))
            iterator += 1
        # 365 homes, on average, in a square mile in Iowa
        self.homes = self.areas.count * 365
        self.feeders = self.homes * .1

    def breed_cats(self) -> None:
        pass
    
    def describe_city(self) -> None:
        print(f"City is {self.areas.count} square miles")
        print(f"Homes in city: {self.homes}")
        print(f"Feeding homes: {self.feeders}")

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
