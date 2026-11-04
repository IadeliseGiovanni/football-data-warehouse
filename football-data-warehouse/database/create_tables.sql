CREATE TABLE dim_team (
    team_id SERIAL PRIMARY KEY,
    team_name VARCHAR(100)
);

CREATE TABLE dim_competition (
    competition_id SERIAL PRIMARY KEY,
    competition_name VARCHAR(100)
);

CREATE TABLE dim_date (
    date_id SERIAL PRIMARY KEY,
    match_date DATE
);

CREATE TABLE fact_matches (
    match_id SERIAL PRIMARY KEY,
    home_team_id INTEGER,
    away_team_id INTEGER,
    competition_id INTEGER,
    date_id INTEGER,
    goals_home INTEGER,
    goals_away INTEGER
);