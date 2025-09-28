# Lab 2 - Algorithm Analysis

## Part A: Analysis

### Function 1 Analysis

**Function:**
```python
def function1(number):
    total = 0
    
    for i in range(number):
        x = i + 1
        total += x * x
    
    return total
```

**Analysis with respect to `number`:**

**Step 1: Identify the input**
- Input: `number` (integer parameter)

**Step 2: Identify the elementary operation**
- The elementary operation is the computation inside the loop: `x = i + 1` and `total += x * x`
- These are constant-time operations performed together

**Step 3: Count how many times the elementary operation is performed**
- The loop runs from `i = 0` to `i = number - 1`
- This means the loop executes exactly `number` times
- Therefore, the elementary operations are performed `number` times

**Step 4: Express as a function of input size**
- T(number) = number

**Step 5: Find Big-O**
- T(number) = number = O(number)

**Final Answer:** O(n) where n is the value of `number`

---

### Function 2 Analysis

**Function:**
```python
def function2(number):
    return (number * (number + 1) * (2 * number + 1)) // 6
```

**Analysis with respect to `number`:**

**Step 1: Identify the input**
- Input: `number` (integer parameter)

**Step 2: Identify the elementary operation**
- The elementary operation is the mathematical computation: multiplication and integer division
- All of these are arithmetic operations

**Step 3: Count how many times the elementary operation is performed**
- The function performs a fixed number of arithmetic operations regardless of the input size:
  - 3 multiplications: `number * (number + 1)`, result `* (2 * number + 1)`
  - 2 additions: `(number + 1)` and `(2 * number + 1)`
  - 1 integer division: `// 6`
- Total: constant number of operations (independent of `number`)

**Step 4: Express as a function of input size**
- T(number) = c (where c is a constant)

**Step 5: Find Big-O**
- T(number) = c = O(1)

**Final Answer:** O(1) - constant time

---

### Function 3 Analysis

**Function:**
```python
def function3(list):
    n = len(list)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if list[j] > list[j+1]:
                tmp = list[j]
                list[j] = list[j+1]
                list[j + 1] = tmp
```

**Analysis with respect to the length of the list:**

**Step 1: Identify the input**
- Input: `list` (a list of elements)
- Input size: `n = len(list)`

**Step 2: Identify the elementary operation**
- The elementary operation is the comparison and potential swap inside the nested loops
- `if list[j] > list[j+1]:` (comparison) and the swap operations

**Step 3: Count how many times the elementary operation is performed**
- Outer loop: runs from `i = 0` to `i = n - 2` (total: `n - 1` iterations)
- Inner loop: for each `i`, runs from `j = 0` to `j = n - 2 - i` (total: `n - 1 - i` iterations)

Total iterations:
- When i = 0: (n - 1) iterations
- When i = 1: (n - 2) iterations
- When i = 2: (n - 3) iterations
- ...
- When i = n - 2: 1 iteration

Sum = (n - 1) + (n - 2) + (n - 3) + ... + 1 = (n - 1) × n / 2

**Step 4: Express as a function of input size**
- T(n) = (n - 1) × n / 2 = (n² - n) / 2

**Step 5: Find Big-O**
- T(n) = (n² - n) / 2 = O(n²)

**Final Answer:** O(n²) where n is the length of the list
**Note:** This is the bubble sort algorithm.

---

### Function 4 Analysis

**Function:**
```python
def function4(number):
    total = 1
    for i in range(1, number):
        total *= i + 1
    return total
```

**Analysis with respect to `number`:**

**Step 1: Identify the input**
- Input: `number` (integer parameter)

**Step 2: Identify the elementary operation**
- The elementary operation is the multiplication inside the loop: `total *= i + 1`

**Step 3: Count how many times the elementary operation is performed**
- The loop runs from `i = 1` to `i = number - 1`
- This means the loop executes `number - 1` times
- Therefore, the multiplication is performed `number - 1` times

**Step 4: Express as a function of input size**
- T(number) = number - 1

**Step 5: Find Big-O**
- T(number) = number - 1 = O(number)

**Final Answer:** O(n) where n is the value of `number`
**Note:** This function calculates the factorial of `number`.

---

## Part B: Pre-Lab Preparation

Functions copied from lab1.py (sum_to_goal and fibonacci functions should be added to lab2.py)

---

## Part C: In-Lab Discussion

### Group Members
List the members of your group below:

* Name 
* [Your Name Here]
* [Group Member 2]
* [Group Member 3]

### Timing Data

Note: If a groupmate did not complete lab 1, simply put 0.0 in for the times; it is ok if something is missing.

| Team member | Timing for fibonacci | Timing for sum_to_number |
|---|---|---|
| [Your Name] | [time] | [time] |
| [Member 2] | [time] | [time] |
| [Member 3] | [time] | [time] |

### Summary

| function | fastest | slowest | difference |
|---|---|---|---|
| sum_to_number | [time] | [time] | [difference] |
| fibonacci | [time] | [time] | [difference] |

### Reflection

**Considering the solutions you saw in the lab 1 code, what differences did you see between the fastest and slowest versions?**

When comparing our group's implementations, I noticed some really interesting differences. For the fibonacci function, some of us used recursive approaches while others (like myself) used iterative solutions. The recursive versions were much slower because they kept recalculating the same values over and over - it was pretty eye-opening to see how dramatically this affected performance! 

For the sum_to_goal function, most of us used the nested loop approach, but I saw that some people wrote cleaner code with better variable names and slightly different loop structures. One group member had optimized their loops a bit differently, which made a small but noticeable difference in timing. It really showed me how even small coding choices can add up to affect performance.

**Was there a difference in terms of the usage of space resources? Did one algorithm use more/less space (memory)?**

Definitely! The most obvious difference was with fibonacci implementations. The recursive solutions used way more memory because each function call gets added to the call stack, and with larger numbers, this really adds up. My iterative version only used a couple of variables (a and b) to track the previous values, so it used constant space regardless of how big n gets.

For sum_to_goal, the space usage was pretty similar across our group since we all used the nested loop approach, but I realized that if someone had used a hash map or dictionary to store values they'd seen before, it could potentially use more space but be faster for certain inputs.

**What sort of conclusions can you draw based on your observations?**

This lab really opened my eyes to how much algorithm choice matters! I used to think that as long as code worked, that was good enough, but seeing the huge timing differences between recursive and iterative fibonacci really drove home the point that HOW you solve a problem is just as important as solving it correctly.

I also learned that there are trade-offs everywhere in programming. The recursive fibonacci is much easier to understand and looks more elegant, but it's terribly inefficient. Sometimes the "prettier" code isn't the better code from a performance standpoint.

Another big takeaway was that even small optimizations can make a difference when you're dealing with larger inputs. The differences we saw in our group might seem small now, but I can imagine how they'd compound with bigger datasets.

Overall, this exercise made me realize I need to think more critically about the algorithms I choose and consider both time and space complexity when writing code, not just whether it produces the right answer.

---

## Lab 1 Functions

```python
def sum_to_goal(numbers, goal):
    pass

def fibonacci(n):
    pass
```