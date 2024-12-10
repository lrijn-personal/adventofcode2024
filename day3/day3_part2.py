import re

file_path = "day3/input.txt"

with open(file_path, 'r') as file:
    input_string = file.read()

pattern = r"mul\((\d+),\s*(\d+)\)|do\(\)|don't\(\)"
matches = re.finditer(pattern, input_string)
enabled = True 
sum = 0

for match in matches:     
    if match.group() == "do()":
        enabled = True
    elif match.group() == "don't()":
        enabled = False

    if enabled:
        if match.group().startswith("mul"):
            # find all numbers in the match
            numbers = re.findall(r'\d+', match.group())
            # Convert the extracted numbers to integers with map funtion
            x, y = map(int, numbers)
            # Multiply the two integers
            result = x * y
            sum += result

print(sum)

