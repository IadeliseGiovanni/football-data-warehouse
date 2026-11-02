from extract.extract_football_api import (
    extract_teams,
    extract_matches
)

teams = extract_teams()

print("\n=== TEAMS ===\n")

print(teams[:1])

matches = extract_matches()

print("\n=== MATCHES ===\n")

print(matches[:1])
