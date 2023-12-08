#Day 2 - Part 1
import re

#Path to the file
file_path = 'C:/Users/bobby/OneDrive/Desktop/AOC/Input2.txt'

# Read the file content
with open(file_path, 'r') as file:
    game_data = file.readlines()

# Function to parse the game data and extract the subsets of cubes shown
def parse_game_data(games):
    game_info = {}
    for game in games:
        # Extracting the game number
        game_number = int(re.search(r"Game (\d+):", game).group(1))
        # Extracting the subsets of cubes
        subsets = re.findall(r"(\d+) red|(\d+) green|(\d+) blue", game)
        # Converting the tuples to dictionary with color counts
        subset_dicts = []
        for subset in subsets:
            color_counts = {
                'red': int(subset[0]) if subset[0] else 0,
                'green': int(subset[1]) if subset[1] else 0,
                'blue': int(subset[2]) if subset[2] else 0,
            }
            subset_dicts.append(color_counts)
        game_info[game_number] = subset_dicts
    return game_info

# Check if the subsets in a game are possible with the given number of cubes
def is_possible(subsets, red, green, blue):
    for subset in subsets:
        if subset['red'] > red or subset['green'] > green or subset['blue'] > blue:
            return False
    return True

# Parse the game data
games = parse_game_data(game_data)

# Determine which games are possible with the given number of cubes
possible_games = []
for game_number, subsets in games.items():
    if is_possible(subsets, 12, 13, 14):
        possible_games.append(game_number)

# Sum of the IDs of possible games
sum_of_ids = sum(possible_games)
sum_of_ids, possible_games


#Part 2
#Function parses the game data to extract the subsets of cubes shown.
def parse_game_data(games):
    game_info = {}
    for game in games:
        # Extracting the game number
        game_number = int(re.search(r"Game (\d+):", game).group(1))
        # Extracting the subsets of cubes
        subsets = re.findall(r"(\d+) red|(\d+) green|(\d+) blue", game)
        # Converting the tuples to dictionary with color counts
        subset_dicts = []
        for subset in subsets:
            color_counts = {
                'red': int(subset[0]) if subset[0] else 0,
                'green': int(subset[1]) if subset[1] else 0,
                'blue': int(subset[2]) if subset[2] else 0,
            }
            subset_dicts.append(color_counts)
        game_info[game_number] = subset_dicts
    return game_info

#Function finds the minimum set of cubes that must have been present for each game.
def find_minimum_set(game_info):
    minimum_sets = {}
    for game_number, subsets in game_info.items():
        # Initializing the minimum counts for each color
        min_red, min_green, min_blue = 0, 0, 0
        for subset in subsets:
            # Updating the minimum counts if the current subset has more cubes of that color
            min_red = max(min_red, subset['red'])
            min_green = max(min_green, subset['green'])
            min_blue = max(min_blue, subset['blue'])
        # Calculating the power of the set
        power = min_red * min_green * min_blue
        minimum_sets[game_number] = power
    return minimum_sets

# Parse the game data
games = parse_game_data(game_data)

# Find the minimum set of cubes for each game and calculate the sum of their powers
minimum_sets = find_minimum_set(games)
sum_of_powers = sum(minimum_sets.values())

sum_of_powers, minimum_sets