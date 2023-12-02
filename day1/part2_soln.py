def find_digits(line, number_map):
    """Extract the first and last digit (or spelled-out number) from the line."""
    # Initialize variables to store the first and last digits
    first_digit = last_digit = None

    # Check each character and the remaining string for matches
    for i in range(len(line)):
        # Check the start of the line for the first digit
        if first_digit is None:
            for number in number_map:
                if line.startswith(number, i):
                    first_digit = number_map[number]
                    break

        # Check the end of the line for the last digit
        if last_digit is None:
            for number in number_map:
                if line.endswith(number, 0, len(line) - i):
                    last_digit = number_map[number]
                    break

        # Break the loop if both digits are found
        if first_digit is not None and last_digit is not None:
            break

    return first_digit, last_digit

def calculate_total_calibration(file_path):
    # Map of spelled-out numbers to their digit equivalents
    number_map = {
        "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
        "six": 6, "seven": 7, "eight": 8, "nine": 9,
        "0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9
    }
    total = 0

    with open(file_path, "r") as file:
        for line in file:
            first_digit, last_digit = find_digits(line.strip(), number_map)
            if first_digit is not None and last_digit is not None:
                total += first_digit * 10 + last_digit

    return total

# Calculate the sum of all calibration values
input_file_path = "input.txt"
print(calculate_total_calibration(input_file_path))
