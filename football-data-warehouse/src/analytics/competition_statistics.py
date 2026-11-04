import pandas as pd

from load.load_postgres import get_engine


def goals_by_competition():

    engine = get_engine()

    query = """
    SELECT
        c.competition_name,
        SUM(f.goals_home + f.goals_away) AS total_goals
    FROM fact_matches f
    JOIN dim_competition c
        ON f.competition_id = c.competition_id
    GROUP BY c.competition_name
    ORDER BY total_goals DESC
    """

    df = pd.read_sql(query, engine)

    print("\n=== GOALS BY COMPETITION ===")
    print(df)

    return df


def matches_by_competition():

    engine = get_engine()

    query = """
    SELECT
        c.competition_name,
        COUNT(*) AS total_matches
    FROM fact_matches f
    JOIN dim_competition c
        ON f.competition_id = c.competition_id
    GROUP BY c.competition_name
    ORDER BY total_matches DESC
    """

    df = pd.read_sql(query, engine)

    print("\n=== MATCHES BY COMPETITION ===")
    print(df)

    return df


def average_goals_by_competition():

    engine = get_engine()

    query = """
    SELECT
        c.competition_name,
        AVG(f.goals_home + f.goals_away) AS average_goals
    FROM fact_matches f
    JOIN dim_competition c
        ON f.competition_id = c.competition_id
    GROUP BY c.competition_name
    ORDER BY average_goals DESC
    """

    df = pd.read_sql(query, engine)

    print("\n=== AVERAGE GOALS BY COMPETITION ===")
    print(df)

    return df