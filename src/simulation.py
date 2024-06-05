from utils import cat
from utils import colony
from utils import city


def main() -> None:

    # Start time in simulation
    time = 0

    # set city size to desired kilometers^2.  Ankeny, Iowa is 76 km^2
    city_size = 76
    sim_city = city.City(city_size)
    # set up a rural area, we don't care how big
    rural_area = city.City(1)

    # setup tracking lists for cats
    homeless_cats = []
    rural_cats = []
    dead_cats = []

    # seed cats in the city and outside it
    seed_cats(10, rural_cats, rural_area)
    seed_cats(6, homeless_cats, sim_city)

    # describe the city cats
    for animal in homeless_cats:
        animal.describe_cat()


def seed_cats(seed_size: int, living_cats: list, sim_city: city.City) -> None:
    # seed number for cats to start simulation
    # representing a number of cats abandoned by owners
    iterator = 1
    while iterator < seed_size:
        area = sim_city.return_random_area()
        temp_cat = cat.Cat(area)
        temp_cat2 = cat.Cat(area)
        living_cats.append(temp_cat)
        living_cats.append(temp_cat2)
        iterator += 2


if __name__ == "__main__":
    main()
