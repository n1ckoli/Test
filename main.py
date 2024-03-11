import math

# Max and min value
with open("10m.txt", "r") as f:
    mass = []
    full_f = f.read()
    for i in full_f.split():
        mass.append(int(i))

print(f"Максимальне значення: {max(mass)}")
print(f"Мінімальне значення: {min(mass)}")

# Median
test_list = [full_f] 
 
test_list = [float(value) for value in full_f.split('\n') if value.isdigit()]

test_list.sort()

mid = len(test_list) // 2
res = (test_list[mid] + test_list[~mid]) / 2

print("Медіана: " + str(res))

# Average
with open(r'10m.txt') as f:
    for line in f:
        fields = line.split()
        rowdata = map(float, fields)
        mass.extend(rowdata)

print(f"Середнє арифметичне: {sum(mass)/len(mass)}")

# Sequences

def increasing_sequence(test):
    with open("10m.txt", 'r') as file:
        numbers = [int(x) for x in file.read().split()]
        
    max_sequence = []
    current_sequence = [numbers[0]]
    
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            current_sequence.append(numbers[i])
        else:
            if len(current_sequence) > len(max_sequence):
                max_sequence = current_sequence
            current_sequence = [numbers[i]]
    
    if len(current_sequence) > len(max_sequence):
        max_sequence = current_sequence
    
    return max_sequence

def decreasing_sequence(test):
    with open("10m.txt", 'r') as file:
        numbers = [int(x) for x in file.read().split()]
        
    max_sequence = []
    current_sequence = [numbers[0]]
    
    for i in range(1, len(numbers)):
        if numbers[i] < numbers[i - 1]: 
            current_sequence.append(numbers[i])
        else:
            if len(current_sequence) > len(max_sequence):
                max_sequence = current_sequence
            current_sequence = [numbers[i]]
    
    
    if len(current_sequence) > len(max_sequence):
        max_sequence = current_sequence
    
    return max_sequence

test = "numbers.txt"  
increasing_sequence = increasing_sequence(test)
decreasing_sequence = decreasing_sequence(test)

print("Послідовність  яка збільшується:", increasing_sequence)
print("Послідовність яка зменьшується:", decreasing_sequence)
