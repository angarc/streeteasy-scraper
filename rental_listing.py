class RentalListing:
    def __init__(
            self,
            address,
            area,
            price,
            net_effective_rent,
            num_beds,
            has_brokers_fee):
        self.address = address
        self.area = area
        self.price = price
        self.num_beds = num_beds
        self.has_fee = has_brokers_fee
        self.net_effective_rent = net_effective_rent

    def __repr__(self):
        return f"RentalListing(\
address={self.address},\
area={self.area},price={self.price},\
net_effective_rent={self.net_effective_rent},\
num_beds={self.num_beds},\
has_fee={self.has_fee})"
