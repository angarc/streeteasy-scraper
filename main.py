from listing_filter_option import ListingFilterOption, Area
from soup_to_listings_adapter import soup_to_listings_adapter

def main():
    opt = ListingFilterOption()
    soup = opt\
            .set_areas([Area.ALL_UPPER_WEST_SIDE])\
            .set_max_price(3300)\
            .set_min_price(2000)\
            .set_max_beds(2)\
            .get()

    listings = soup_to_listings_adapter(soup)

    for list in listings:
        print(repr(list))
        print()


if __name__ == '__main__':
    main()
