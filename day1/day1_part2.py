def calculate_score(column1, column2):
    score = 0
    for num in column1:
        if num in column2:
            count = column2.count(num)
            score += num * count
    return score

def read_columns(file_path):
    column1 = []
    column2 = []
    
    with open(file_path, 'r') as file:
        for line in file:
            num1, num2 = line.split()
            column1.append(int(num1))
            column2.append(int(num2))
            
    return column1, column2

if __name__ == "__main__":
    file_path = "day1/input.txt"
    col1, col2 = read_columns(file_path)
    final_score = calculate_score(col1, col2)
    print(f"Score: {final_score}")
