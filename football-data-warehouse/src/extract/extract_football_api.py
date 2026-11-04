import requests


API_KEY = "f7ac561eedfd47ba9b34b496eb95f334"

HEADERS = {
    "X-Auth-Token": API_KEY
}


def extract_matches():

    url = "https://api.football-data.org/v4/matches"

    response = requests.get(
        url,
        headers=HEADERS
    )

    response.raise_for_status()

    data = response.json()

    return data["matches"]


def extract_teams():

    url = "https://api.football-data.org/v4/teams"

    response = requests.get(
        url,
        headers=HEADERS
    )

    response.raise_for_status()

    data = response.json()

    return data["teams"]