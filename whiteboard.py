# WEEK-2 DAY-2 WHITE BOARD:
# Write a function that takes a positive integer and then calculates and returns the sum of all numbers from 1 up to the positive integer.
# Example : Input of 5 would return 15.
# 1+2+3+4+5 = 15

def sumAll(num):
    sum = 0
    for x in range(1, num + 1):
        sum += x
    return sum
print(sumAll(5))