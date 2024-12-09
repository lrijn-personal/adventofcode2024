file_path = "day2/input.txt"


safe_counter = 0

with open(file_path, 'r') as file:
    for line in file:
        boolean = True
        line = line.strip()
        line = line.split(" ")
        for i in range(len(line)-1):
            current = int(line[i])
            next = int(line[i+1])
            # print(f"current: {current}, next: {next}")
            if i == 0:
                # First pair determines if we check for increasing or decreasing
                is_increasing = int(line[0]) < int(line[1])
            
            if is_increasing and current >= next:
                boolean = False
                break
            elif not is_increasing and current <= next:
                boolean = False
                break
            elif current > next:
                difference = current - next

            elif next > current:
                difference = next - current

            elif current == next:
                difference = 0

            if  not (difference >= 1 and difference <= 3):
                boolean = False
                break

        if boolean:
            safe_counter += 1
            print(f"line:{line}, safe")
        else:
            print(f"line:{line}, unsafe")

print(f"there are {safe_counter} safe lines")