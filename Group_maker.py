import random

# List of teams
teams = ['Red Army FC', 'Kasanoma FC', 'Northside FC','Legends United FC', 'Highlanders FC', 'Elite FC']


random.shuffle(teams)

group_1 = teams[:3]  # First three teams
group_2 = teams[3:]  # Last three teams

print("Group 1:", group_1)
print("Group 2:", group_2)