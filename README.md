# streeteasy-scraper
[![license](https://img.shields.io/badge/license-MIT-brightgreen)]()

[![issue tracker](https://img.shields.io/github/issues/angarc/streeteasy-scraper)]()

## Overview
streeteasy-scraper is an api for you to use in your projects that can provide current information on vacant rental units in NYC.

5 Testable Features:

Filter rental units by:

1. Mininum price
2. Maximum price
3. Maximum number of bedrooms
4. Whether or not rental has a brokers fee
5. What area of manhattan the unit is located in

To see how to configure these filters when looking for units, look at the `setUp()` function in the `test_soup.py` test file.

## Testing

```
python3 -m unittest test_soup.py
python3 -m unittest test_soup_integration.py
```

To generate code coverage report:

```
$ python -m coverage run -m unittest discover
$ python -m coverage html
```

