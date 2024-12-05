file_path = "day1/input.txt"
column1= []
column2= []

with open(file_path, 'r') as file:
    for line in file:
        int1, int2 = line.split()
        column1.append(int(int1))
        column2.append(int(int2))

score = 0
for i in column1:
    if i in column2:
        count = column2.count(i)
        score += i * count
        # print(f"number: {i}, count: {count}, score: {score}")

print(f"Score: {score}")
