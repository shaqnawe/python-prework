# Question 1. 
# Function to print username
def hello_name(user_name):
    print(f"hello_{user_name}!")
hello_name('Shakti')

# Question 2.
# Function to odd numbers from 1-100
def first_odds():
    num = 0
    while(num<100):
        num += 1
        if(num % 2 != 0):
            print(num)
        else:
            continue

print(first_odds())

# Question 3. 
# Function to return MAX number in a list
def max_num_in_list(a_list):
    max_num = 0
    for num in a_list:
        if(num > max_num):
            max_num = num
            # Print the current max_num
            # print(max_num)
        else:
            continue
    return max_num

print(max_num_in_list([2,5,-3,10,70,23,89,-66,9,100,54,5,8,44]))

# Question 4. 
# Function to return a leap year
def is_leap_year(a_year):
    if(((a_year % 4 == 0) and (a_year % 100 != 0)) or (a_year % 400 == 0)):
        return True
    else:
        return False

print(is_leap_year(1924))

# Question 5. 
# Function to check if numbers in a list are consecutive
def is_consecutive(a_list):
    # Sort the given list
    sorted_list = sorted(a_list)
    # Create a test list using min and max+1 (as range excludes the last number) of "a_list"
    test_list = list(range(min(a_list), max(a_list)+1))
    # print(sorted_list)
    # print(range_list)
    if sorted_list == test_list:
        return True
    else:
        return False

print(is_consecutive([11,15,12,16,14,13,19,20,17,18]))
    