# Countdown 

def some_num(num): 
    output = []
    for i in range(num,-1,-1):
        output.append(i)
    return output

print(some_num(5))


# Print and Return

def print_and_return(some_list):
    print(some_list[0])
    return some_list[1]

print(print_and_return([1,2]))



# First Plus Length

def first_plus_length(some_list):
    return some_list[0] + len(some_list)

print(first_plus_length([1,2,3,4,5]))



# Values Greater than Second 

def values_greater_than_second(list):
    if len(list) < 2:
        return False
    output = []
    for i in range(0,len(list)):
        if list[i] > list[1]:
            output.append(list[i])
    print(len(output))
    return output
print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))



# This Length, That Value

def length_and_value(size,value):
    my_list = []
    for i in range(0,size):
        my_list.append(value)
    return my_list

print(length_and_value(4,7))
# should return [7,7,7,7]
print(length_and_value(6,2))
# should return [2,2,2,2,2,2]
