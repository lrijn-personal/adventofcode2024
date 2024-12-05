file_path = "day1/input.txt"
column1= []
column2= []

with open(file_path, 'r') as file:
    for line in file:
        int1, int2 = line.split()
        column1.append(int(int1))
        column2.append(int(int2))

column1.sort()  
column2.sort()

total_distance = 0
for i in range(len(column1)):
    if column1[i] > column2[i]:
        distance = column1[i] - column2[i]
    else:
        distance = column2[i] - column1[i]
    # print(f"column1: {column1[i]}, column2: {column2[i]}, Distance: {distance}")
    total_distance += distance

print(f"Total distance: {total_distance}")
