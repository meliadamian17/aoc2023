import time

start_time = time.time()
f = open("input.txt", "r") #opening file

total = 0
while True:
    line = f.readline()
    if not line:
        break
    line_digits = [i for i in line if i.isdigit()] #making list of all digits in line, slow, but looks clean
    total += int(line_digits[0] + line_digits[-1]) #concatenating first and last digits before converting to int and adding to total

end_time = time.time()
print(end_time - start_time)