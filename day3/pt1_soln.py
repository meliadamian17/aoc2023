symbols = "!@#$%^&*()_+{}[]:;\"'\\|,/<>?`~"

# f = open("day3/input.txt", "r")
# lines = [line.split() for line in f.readlines()]

f = open("day3/input.txt", "r")

#make a list of lines from f
lines = [line.strip('\n') for line in f.readlines()]


def find_nums_in_line(line):
    nums = []
    num = ""
    for char in line:
        if char.isdigit():
            num += char
        elif num != "":
            nums.append(int(num))
            num = ""
        if num:
            nums.append(int(num))
    
    return nums

def find_symbols_in_line(line):
    #return list of indices of symbols in line
    symbol_locs = []
    for i in range(len(line)):
        if line[i] in symbols:
            symbol_locs.append(i)
    return symbol_locs

total = 0

for i in range(len(lines)):
    nums = find_nums_in_line(lines[i])
    
    sym_locs = find_symbols_in_line(lines[i])
    num_locs = [(lines[i].index(str(num)),lines[i].index(str(num))+len(str(num))-1) for num in nums]

    
    for k in range(len(nums)):
        for sym in sym_locs:
            if sym >= num_locs[k][0]-1 and sym <= num_locs[k][1]+1:
                total += nums[k]
                break
    # print(num_locs)
    if i == 0:
        for j in range(len(nums)):
            line = lines[i+1]
            next_sym_locs = find_symbols_in_line(line)
            #check if any of the symbols are in the range of each tuple in num_locs, if so, add num to total
            for sym_loc in next_sym_locs:
                if sym_loc >= num_locs[j][0]-1 and sym_loc <= num_locs[j][1]+1:
                    total += nums[j]
                
                    break
    elif i == len(lines)-1:
        for j in range(len(nums)):
            line = lines[i-1]
            prev_sym_locs = find_symbols_in_line(line)
            #check if any of the symbols are in the range of each tuple in num_locs, if so, add num to total
            for sym_loc in prev_sym_locs:
                if sym_loc >= num_locs[j][0]-1 and sym_loc <= num_locs[j][1]+1:
                    total += nums[j]
                    break
    
    else:
        for j in range(len(nums)):
            line1 = lines[i-1]
            line2 = lines[i+1]
            prev_sym_locs = find_symbols_in_line(line1)
            next_sym_locs = find_symbols_in_line(line2)
            for sym_loc in prev_sym_locs:
                if sym_loc >= num_locs[j][0]-1 and sym_loc <= num_locs[j][1]+1:
                    total += nums[j]
                    break
            for sym_loc in next_sym_locs:
                if sym_loc >= num_locs[j][0]-1 and sym_loc <= num_locs[j][1]+1:
                    total += nums[j]
                    break   
    # print(total)     

print(total)