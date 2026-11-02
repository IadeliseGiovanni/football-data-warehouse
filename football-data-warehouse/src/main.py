from extract.extract_matches import extract_data
from transform.transform_matches import transform_data

from load.load_postgres import get_engine

from load.load_dw import (
    clear_dw,
    load_dimensions,
    load_fact_matches
)

from analytics.team_statistics import (
    top_scoring_teams,
    match_count,
    average_goals
)

from analytics.competition_statistics import (
    goals_by_competition,
    matches_by_competition,
    average_goals_by_competition
)


print("=== PIPELINE AVVIATA ===")


# EXTRACT

data = extract_data()


# TRANSFORM

df = transform_data(data)


# LOAD STAGING

engine = get_engine()

df.to_sql(
    "users_staging",
    engine,
    if_exists="append",
    index=False
)

print("Users Staging caricata")


# LOAD DW

clear_dw()

load_dimensions()

load_fact_matches()

print("Data Warehouse caricato")


# TEAM ANALYTICS

top_scoring_teams()

match_count()

average_goals()


# COMPETITION ANALYTICS

goals_by_competition()

matches_by_competition()

average_goals_by_competition()


print("=== PIPELINE COMPLETATA ===")