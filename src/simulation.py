from utils import city


def main() -> None:

    # Start time in simulation, 1 is equal to 4 months to match up to average cat pregnancy cycle. three cycles per year
    time = 0
    # run for 5 years
    cycles = 15 

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
    sim_city.seed_cats(10, rural_cats)
    rural_area.seed_cats(6, homeless_cats)

    while time < cycles:
        sim_city.seed_cats(10, rural_cats)
        rural_area.seed_cats(6, homeless_cats)
        time += 1

    # describe the city cats
    for animal in homeless_cats:
        animal.describe_cat()


if __name__ == "__main__":
    main()
