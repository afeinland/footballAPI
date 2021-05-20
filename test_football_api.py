import requests
import pytest

URI = 'https://api.football-data.org/v2/teams/12'
headers = {'X-Auth-Token': 'e051043b86624518a57a263f9388d198'}


@pytest.fixture()
def response():
    return requests.get(URI, headers=headers)


def test_successful_response(response):
    assert response.status_code == 200


def test_failed_authentication():
    response = requests.get(URI)
    assert response.status_code == 403


def test_more_than_20_squad_members(response):
    squad = response.json()["squad"]
    assert len(squad) > 20
