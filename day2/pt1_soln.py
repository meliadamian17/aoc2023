import re
'''Determine which games would have been possible 
if the bag had been loaded with only 
12 red cubes, 
13 green cubes, 
and 14 blue cubes. 
What is the sum of the IDs of those games?'''


def parse_line(line, red_limit, green_limit, blue_limit):
    #basically digit(s) followed by whitespace followed by color
    pattern = r"(\d+)\s*(red|green|blue)"
    matches = re.findall(pattern, line)

    #get max count of each color
    red_max = max((int(num) for num, color in matches if color == "red"), default=0)
    green_max = max((int(num) for num, color in matches if color == "green"), default=0)
    blue_max = max((int(num) for num, color in matches if color == "blue"), default=0)
    
    return red_max <= red_limit and green_max <= green_limit and blue_max <= blue_limit

with open("day2/input.txt", "r") as f:
    valid_games = []
    game_id = 1
    for line in f:
        if parse_line(line, 12, 13, 14):
            print(line)
            valid_games.append(game_id)
        game_id += 1



print(valid_games)
print(sum(valid_games))