import pandas as pd

from sqlalchemy import text

from load.load_postgres import get_engine


def clear_dw():

    engine = get_engine()

    with engine.begin() as conn:

        conn.execute(
            text(
                """
                TRUNCATE TABLE
                    fact_matches,
                    dim_team,
                    dim_competition,
                    dim_date
                RESTART IDENTITY CASCADE
                """
            )
        )

    print("✅ Data Warehouse pulito")


def load_teams():

    engine = get_engine()

    teams = [
        "Napoli",
        "Inter",
        "Milan",
        "Juventus",
        "Roma"
    ]

    team_df = pd.DataFrame({
        "team_name": teams
    })

    team_df.to_sql(
        "dim_team",
        engine,
        if_exists="append",
        index=False
    )

    print("✅ Dim Team caricata")


def load_competitions():

    engine = get_engine()

    competitions = [
        "Serie A",
        "Champions League",
        "Europa League"
    ]

    competition_df = pd.DataFrame({
        "competition_name": competitions
    })

    competition_df.to_sql(
        "dim_competition",
        engine,
        if_exists="append",
        index=False
    )

    print("✅ Dim Competition caricata")


def load_dates():

    engine = get_engine()

    dates = [
        "2026-11-01",
        "2026-11-02",
        "2026-11-03"
    ]

    date_df = pd.DataFrame({
        "match_date": dates
    })

    date_df.to_sql(
        "dim_date",
        engine,
        if_exists="append",
        index=False
    )

    print("✅ Dim Date caricata")


def load_fact_matches():

    engine = get_engine()

    matches = [
        {
            "home_team_id": 1,
            "away_team_id": 2,
            "competition_id": 1,
            "date_id": 1,
            "goals_home": 2,
            "goals_away": 1
        },
        {
            "home_team_id": 2,
            "away_team_id": 3,
            "competition_id": 1,
            "date_id": 2,
            "goals_home": 1,
            "goals_away": 1
        }
    ]

    matches_df = pd.DataFrame(matches)

    matches_df.to_sql(
        "fact_matches",
        engine,
        if_exists="append",
        index=False
    )

    print("✅ Fact Matches caricata")


def load_dimensions():

    load_teams()

    load_competitions()

    load_dates()

    print("✅ Dimensioni caricate")