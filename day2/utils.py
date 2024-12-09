def check_safe_or_unsafe(line):
    condition = "safe"
    for i in range(len(line)-1):
        current = int(line[i])
        next = int(line[i+1])
        if i == 0:
            # First pair determines if we check for increasing or decreasing
            is_increasing = line[0] < line[1]
            
        if is_increasing and current >= next:
            condition = "unsafe"        
            break
        elif not is_increasing and current <= next:
            condition = "unsafe"
            break
        elif current > next:
            difference = current - next

        elif next > current:
            difference = next - current

        elif current == next:
            difference = 0

        if  not (difference >= 1 and difference <= 3):
            condition = "unsafe"
            break
    return condition