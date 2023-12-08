def calculate_ways(time, record_distance):
    ways_to_win = 0
    for hold_time in range(time + 1):
        speed = hold_time
        travel_time = time - hold_time
        distance = speed * travel_time
        if distance > record_distance:
            ways_to_win += 1
    return ways_to_win

# Race details
races = [
    {"time": 54, "record_distance": 302},
    {"time": 94, "record_distance": 1476},
    {"time": 65, "record_distance": 1029},
    {"time": 92, "record_distance": 1404}
]

# Calculate ways to win for each race
ways_to_win_per_race = [calculate_ways(race["time"], race["record_distance"]) for race in races]

# Multiply the ways to win for all races
total_ways_to_win = 1
for ways in ways_to_win_per_race:
    total_ways_to_win *= ways

total_ways_to_win, ways_to_win_per_race
