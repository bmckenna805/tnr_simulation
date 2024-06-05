import random


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

    def return_random_area(self) -> str:
        return random.choice(self.areas)
