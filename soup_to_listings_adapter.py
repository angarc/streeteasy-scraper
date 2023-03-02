from rental_listing import RentalListing


def soup_to_listings_adapter(soup):
    listing_soups = soup.findAll('li', 'searchCardList--listItem')
    listings = []

    for listing in listing_soups:
        address = listing.address.text.strip()
        price = listing.find_all(
            'span', 'listingCard-priceMargin')[0].text.strip()
        area = listing.find_all(
            'p', 'listingCard-upperShortLabel')[0].text.strip()
        num_beds = listing.find_all('div', 'listingDetailDefinitions')[
            0].find_all('span')[1].text
        has_fee = len(listing.find_all('span', 'NoFeeBadge--SRPCard')) == 0

        net_effective_rent = "$0"
        listing_summary = listing.find_all('p', 'listingCardBottom-summary')
        if len(listing_summary) > 0:
            net_effective_rent = listing_summary[0].b.text

        listings.append(
            RentalListing(
                address,
                area,
                price,
                net_effective_rent,
                num_beds,
                has_fee))

    return listings
