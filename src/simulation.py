from utils import city


def main() -> None:
    # Start time in simulation, 1 is equal to 4 months to match up to
    # average cat pregnancy cycle. three cycles per year
    time = 0
    # run for 5 years
    cycles = 15

    # set up a rural area, we don't care how big
    rural_area = city.City()
    # set city size to desired kilometers^2.  Ankeny, Iowa is 76 km^2
    city_size = 76
    sim_city = city.City(city_size)

    # setup tracking lists for cats
    homeless_cats = []
    rural_cats = []
    dead_cats = []

    # seed cats in the city and outside it
    sim_city.seed_cats(10, homeless_cats)
    rural_area.seed_cats(3, rural_cats)

    while time < cycles:
        # simulate further abandonment of cats
        sim_city.seed_cats(4, homeless_cats)
        rural_area.seed_cats(1, rural_cats)
        # migrate cats between rural and city

        # all moms from previous time slice give birth

        # breed cats in areas
        sim_city.breed_cats(homeless_cats)
        rural_area.breed_cats(rural_cats)
        # age all cats in all areas
        sim_city.age_all_cats(homeless_cats)
        rural_area.age_all_cats(rural_cats)
        # cats pass away due to causes

        # increment time
        time += 1

    # describe the areas and city cats
    sim_city.describe_city()
    rural_area.describe_city()
    print(f"Homeless Cats: {len(homeless_cats)}")
    # for animal in homeless_cats:
    #    animal.describe_cat()
    print(f"Rural Cats: {len(rural_cats)}")


if __name__ == "__main__":
    main()
