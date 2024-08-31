import itertools
import random

# List of teams
teams = ['Red Army FC', 'Kasanoma FC', 'Northside FC', 'Legends United FC', 'Highlanders FC', 'Elite FC']


all_fixtures = list(itertools.combinations(teams, 2))

random.shuffle(all_fixtures)


fixtures_dict = {team: [] for team in teams}

for team1, team2 in all_fixtures:  
    fixtures_dict[team1].append(f"{team1} vs {team2}")  
    fixtures_dict[team2].append(f"{team2} vs {team1}")

selected_team = input("Enter the team name to view its fixtures: ").strip()

if selected_team in fixtures_dict:
    print(f"\nFixtures for {selected_team}:")
    for fixture in fixtures_dict[selected_team]:
        print(fixture)
else:
    print("Team not found. Please check the name and try again.")