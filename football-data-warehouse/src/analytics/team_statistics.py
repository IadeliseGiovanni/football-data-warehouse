import pandas as pd

from load.load_postgres import get_engine


def top_scoring_teams():

    engine = get_engine()

    query = """
    SELECT
        h.team_name,
        SUM(f.goals_home) AS totale_gol
    FROM fact_matches f
    JOIN dim_team h
        ON f.home_team_id = h.team_id
    GROUP BY h.team_name
    ORDER BY totale_gol DESC
    """

    df = pd.read_sql(query, engine)

    print("\n=== TOP SCORING TEAMS ===")
    print(df)

    return df


def match_count():

    engine = get_engine()

    query = """
    SELECT
        h.team_name,
        COUNT(*) AS partite_giocate
    FROM fact_matches f
    JOIN dim_team h
        ON f.home_team_id = h.team_id
    GROUP BY h.team_name
    ORDER BY partite_giocate DESC
    """

    df = pd.read_sql(query, engine)

    print("\n=== MATCH COUNT ===")
    print(df)

    return df


def average_goals():

    engine = get_engine()

    query = """
    SELECT
        h.team_name,
        AVG(f.goals_home) AS media_gol
    FROM fact_matches f
    JOIN dim_team h
        ON f.home_team_id = h.team_id
    GROUP BY h.team_name
    ORDER BY media_gol DESC
    """

    df = pd.read_sql(query, engine)

    print("\n=== AVERAGE GOALS ===")
    print(df)

    return df