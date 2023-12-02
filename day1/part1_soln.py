#open the input file that is in the current directory
import time
f = open("input.txt", "r")

start_time = time.time()

sum = 0

while True:
    #read the first line of the file
    line = f.readline()
    #if the line is empty, you are done with all lines in the file
    if not line:
        break
    first_digit = -1
    last_digit = -1
    for i in range(len(line)):
        if line[i].isdigit() and first_digit == -1:
            first_digit = line[i]
        else:
            if line[i].isdigit():
                last_digit = line[i]
        if last_digit == -1:
            last_digit = first_digit

    linevalue = int(first_digit + last_digit)
    sum += linevalue

end_time = time.time()

print(end_time - start_time)



            


