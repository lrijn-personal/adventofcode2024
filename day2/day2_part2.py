from utils import check_safe_or_unsafe

file_path = "day2/input.txt"
safe_counter = 0

with open(file_path, 'r') as file:
    for line in file:
        boolean = True
        line = line.strip()
        line = line.split(" ")
        line = [int(i) for i in line]
        condition = check_safe_or_unsafe(line)
        if condition == "safe":
            safe_counter += 1
        if condition == "unsafe":
            for i in range(len(line)):
                new_line = line.copy()
                new_line.pop(i)
                condition = check_safe_or_unsafe(new_line)
                if condition == "safe":
                    safe_counter += 1
                    break
        
        print(f"line: {line}, condition: {condition}")

print(f"safe_counter: {safe_counter}")