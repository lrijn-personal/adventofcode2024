import re

file_path = "day3/input.txt"

with open(file_path, 'r') as file:
    input_string = file.read()

pattern = r'mul\((\d+),(\d+)\)'
matches = re.findall(pattern, input_string)
sum = 0
for match in matches:
    sum_match = (int(match[0]) * int(match[1]))
    sum += sum_match

print(sum)