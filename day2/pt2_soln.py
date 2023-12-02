import re
'''Determine which games would have been possible 
if the bag had been loaded with only 
12 red cubes, 
13 green cubes, 
and 14 blue cubes. 
What is the sum of the IDs of those games?'''

def parse_line(line):
    #basically digit(s) followed by whitespace followed by color
    pattern = r"(\d+)\s*(red|green|blue)"
    matches = re.findall(pattern, line)

    #get max count of each color
    red_max = max((int(num) for num, color in matches if color == "red"), default=0)
    green_max = max((int(num) for num, color in matches if color == "green"), default=0)
    blue_max = max((int(num) for num, color in matches if color == "blue"), default=0)
    
    return red_max * green_max * blue_max

with open("day2/input.txt", "r") as f:
    total = 0
    for line in f:
        total += parse_line(line)

print(total)
