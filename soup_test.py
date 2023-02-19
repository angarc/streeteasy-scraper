from listing_filter_option import ListingFilterOption, Area
from soup_to_listings_adapter import soup_to_listings_adapter
import unittest

class TestSoups(unittest.TestCase):
    def setUp(self):
        self.min_price = 2000
        self.max_price = 3500
        self.max_beds  = 1
        self.has_fee   = False
        self.areas     = [Area.ALL_UPPER_WEST_SIDE]

        self.opt = ListingFilterOption()
        soup = self.opt\
            .set_areas(self.areas)\
            .set_max_price(self.max_price)\
            .set_min_price(self.min_price)\
            .set_max_beds(self.max_beds)\
            .set_has_brokers_fee(self.has_fee)\
            .get()

        self.listings = soup_to_listings_adapter(soup)


    def test_min_price(self):
        for listing in self.listings:
            price = int(listing.price[1:].replace(',',''))
            self.assertGreaterEqual(price, self.min_price)


    def test_max_price(self):
        for listing in self.listings:
            price = int(listing.price[1:].replace(',',''))
            net_effective_rent = int(listing.net_effective_rent[1:].replace(',',''))
            self.assertTrue(price < self.max_price or net_effective_rent < self.max_price)


    def test_max_beds(self):
        for listing in self.listings:
            self.assertTrue(listing.num_beds == "1 Bed" or listing.num_beds == "Studio")


    def test_area(self):
        for listing in self.listings:
            index = listing.area.index("in")
            area = listing.area[index+3:]

            self.assertTrue(area == "Lincoln Square" or area == "Upper West Side" or area == "Manhattan Valley")


    def test_has_fee(self):
        for listing in self.listings:
            self.assertEqual(listing.has_fee, self.has_fee)

