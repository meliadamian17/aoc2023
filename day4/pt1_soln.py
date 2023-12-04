f = open("day4/input.txt", "r")

wins = 0

for line in f:
    line = line[line.find(":")+2:]
    # win = [int(num) for num in line[:line.find("|")].rstrip().split(" ") if num != ""]
    # nums = [int(num) for num in line[line.find("|")+2:].lstrip().strip("\n").split(" ") if num != ""]
    wins += 2**(len([val for val in [int(num) for num in line[:line.find("|")].rstrip().split(" ") if num != ""] if val in [int(num) for num in line[line.find("|")+2:].lstrip().strip("\n").split(" ") if num != ""]])-1) if len([val for val in [int(num) for num in line[:line.find("|")].rstrip().split(" ") if num != ""] if val in [int(num) for num in line[line.find("|")+2:].lstrip().strip("\n").split(" ") if num != ""]]) > 0 else 0
    
print(wins)