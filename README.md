# streeteasy-scraper
[![license](https://img.shields.io/badge/license-MIT-brightgreen)]()

[![issue tracker](https://img.shields.io/github/issues/angarc/streeteasy-scraper)]()

[![codecov](https://img.shields.io/codecov/c/github/angarc/streeteasy-scraper)]()

[![build](https://img.shields.io/github/actions/workflow/status/angarc/streeteasy-scraper/build_status.yml)]()

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

**IMPORTANT:** I'm using [Pipenv](https://github.com/pypa/pipenv) for this project. I've included all the libraries/commands you need to 
test and autoformat in the Pipfile. To get this running:

```
$ pipenv install
```

---

To run the tests:

```
$ pipenv run python3 -m unittest test_soup.py
$ pipenv run python3 -m unittest test_soup_integration.py
```

To generate code a coverage report, run these 2 lines in this order:

```
$ pipenv run python -m coverage run -m unittest discover
$ pipenv run python -m coverage report
```

## Autoformat

To check if there are pep8 violations in the code, run:

```
$ pipenv run flake8
```

To fix 99% of these errors, run:

```
$ pipenv run autopep8 --in-place --aggressive --aggressive -r .
```
