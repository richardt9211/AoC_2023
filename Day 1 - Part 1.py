import re

def calculate_calibration_sum(lines):
    total_sum = 0
    for line in lines:
        # Find all digits in the line
        digits = re.findall(r'\d', line)

        if digits:
            # Extract the first and last digit
            first_digit = digits[0]
            last_digit = digits[-1]

            # Combine to form a two-digit number and add to total sum
            total_sum += int(first_digit + last_digit)

    return total_sum

# Read in Input file
file_path = 'C://Users//bobby//OneDrive//Desktop//AOC//input1.txt'

with open(file_path, 'r') as file:
    lines = file.readlines()
    
# Calculate the sum of calibration values
calibration_sum = calculate_calibration_sum(lines)
calibration_sum