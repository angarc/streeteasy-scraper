from enum import Enum
from soups import get_page_html

class Area(Enum):
    ALL_UPPER_WEST_SIDE = 135
    LINCOLN_SQUARE = 136
    UPPER_WEST_SIDE = 137
    MANHATTAN_VALLEY = 138
    ALL_UPPER_EAST_SIDE = 139
    UPPER_EAST_SIDE = 140
    LENOX_HILL = 141

class ListingFilterOption:
    def __init__(self):
        self.min_price = 0
        self.max_price = 0
        self.areas = []
        self.max_beds = None
        self.has_fee = True


    def set_max_beds(self, max_beds):
        self.max_beds = max_beds
        return self


    def set_min_price(self, price):
        self.min_price = price
        return self


    def set_max_price(self, price):
        self.max_price = price
        return self


    def set_areas(self, areas):
        self.areas = areas
        return self

    
    def set_has_brokers_fee(self, has_fee):
        self.has_fee = has_fee
        return self


    def get(self):
        url = f"https://streeteasy.com/for-rent/nyc/{self._price_filter_format()}{self._area_filter_format()}{self._max_beds_filter_format()}{self._no_fee_filters()}"
        html = get_page_html(url)

        return html

        
    def _price_filter_format(self):
        if not self.min_price and not self.max_price:
            return ""

        return f"price:{self.min_price}-{self.max_price}|"


    def _area_filter_format(self):
        return f"area:{','.join([str(area.value) for area in self.areas])}|"


    def _max_beds_filter_format(self):
        if not self.max_beds:
            return ""

        return f"beds<={self.max_beds}|"

    
    def _no_fee_filters(self):
        if self.has_fee == True:
            return ""

        return "no_fee:1|"

