# 1 - Countdown 

def countdown_list(num):
    countDown_list = [] 
    for i in range(num, -1, -1):
        countDown_list.append(i)
    return countDown_list
num = int(input("Enter a number: ")) 
result = countdown_list(num) 
print(result)

# 2 - Print and Return 

def print_and_return(numbers):
    print(numbers[0])  
    return numbers[1]  
result = print_and_return([0,1])
print(result)

# 3 First Plus Length

def first_plus_length(x):
    return x[0] + len(x)
result = first_plus_length([1,2,3])
print(result)

# 4 Values Greater than Second

def values_greater_than_second(lst):
    if len(lst) < 2:
        return False
    second_value = lst[1]
    new_list = [x for x in lst if x > second_value]
    
    print(len(new_list))
    
    return new_list

result1 = values_greater_than_second([5, 2, 3, 2, 1, 4])  
print(result1)

result2 = values_greater_than_second([3])                 
print(result2)

# 5 This Length, That Value

def length_and_value(size, value):

    return [value] * size

result1 = length_and_value(4, 7)
print(result1)

result2 = length_and_value(6, 2)  
print(result2)
