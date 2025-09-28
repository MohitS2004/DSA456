

def sum_to_goal(numbers, goal):
    """
    Function from lab1: finds two numbers that sum to goal and returns their product
    """
    length = len(numbers)
    for i in range(length):
        for j in range(i + 1, length):
            if numbers[i] + numbers[j] == goal:
                return numbers[i] * numbers[j]
    return 0

def fibonacci(n):
    """
    Function from lab1: calculates the nth Fibonacci number iteratively
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def function1(number):
    """Function 1 from the analysis - calculates sum of squares"""
    total = 0
    
    for i in range(number):
        x = i + 1
        total += x * x
    
    return total

def function2(number):
    """Function 2 from the analysis - mathematical formula for sum of squares"""
    return (number * (number + 1) * (2 * number + 1)) // 6

def function3(list):
    """Function 3 from the analysis - bubble sort algorithm"""
    n = len(list)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if list[j] > list[j+1]:
                tmp = list[j]
                list[j] = list[j+1]
                list[j + 1] = tmp

def function4(number):
    """Function 4 from the analysis - factorial calculation"""
    total = 1
    for i in range(1, number):
        total *= i + 1
    return total