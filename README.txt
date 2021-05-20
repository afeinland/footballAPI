A small script to validate the following functionality:

- Validate 200 http code on successful response
- Validate 403 http code on failed authentication
- Validate more than 20 squad members are there in API response

Endpoint: https://api.football-data.org/v2/teams/12

To run tests:
1. $ pip install requests pytest
2. $ pytest -v test_football_api.py
