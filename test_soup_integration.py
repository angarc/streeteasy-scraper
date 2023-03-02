from listing_filter_option import ListingFilterOption, Area
from soup_to_listings_adapter import soup_to_listings_adapter
import unittest


class TestSoups(unittest.TestCase):
    def test_request_flow(self):
        opt = ListingFilterOption()
        soup = opt\
            .set_areas([Area.ALL_UPPER_WEST_SIDE])\
            .set_max_price(3500)\
            .set_min_price(2300)\
            .set_max_beds(2)\
            .set_has_brokers_fee(True)\
            .get()

        listings = soup_to_listings_adapter(soup)

        for listing in listings:
            price = int(listing.price[1:].replace(',', ''))
            net_effective_rent = int(
                listing.net_effective_rent[1:].replace(',', ''))
            num_beds = listing.num_beds

            index = listing.area.index("in")
            area = listing.area[index + 3:]

            self.assertTrue(price <= 3500 or net_effective_rent <= 3500)
            self.assertGreaterEqual(price, 2300)
            self.assertTrue(num_beds == "1 Bed" or num_beds ==
                            "2 Beds" or num_beds == "Studio")
            self.assertTrue(area == "Lincoln Square" or area ==
                            "Upper West Side" or area == "Manhattan Valley")
