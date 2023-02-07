def find_minVal(target_list):
    min = target_list[0]

    for num in target_list:
        if num < min:
            min = num
    
    return min

def find_maxVal(target_list):
    max = target_list[0]

    for num in target_list:
        if num > max:
            max = num
    
    return max


num_list = [10, 55, 23, 2, 79, 101, 16, 82, 30, 45]

print("min value is " + str(find_minVal(num_list)))
print("max value is " + str(find_maxVal(num_list)))