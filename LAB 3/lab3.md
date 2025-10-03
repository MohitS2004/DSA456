# Lab 3 Analysis and Reflection

## Part B: Analysis of Recursive Functions

### Function 1 Analysis

```python
def function1(value, number):
    if (number == 0):
        return 1
    elif (number == 1):
        return value
    else:
        return value * function1(value, number-1)
```

**Analysis with respect to `number`:**

**Step 1: Identify the basic operation**
The basic operation is multiplication (`*`).

**Step 2: Set up the recurrence relation**
Let T(n) = number of multiplications for input `number = n`

- T(0) = 0 (base case, no multiplication)
- T(1) = 0 (base case, no multiplication)
- T(n) = 1 + T(n-1) for n > 1 (one multiplication plus recursive call)

**Step 3: Solve the recurrence**
T(n) = 1 + T(n-1)
     = 1 + (1 + T(n-2))
     = 2 + T(n-2)
     = 3 + T(n-3)
     = ...
     = (n-1) + T(1)
     = (n-1) + 0
     = n-1

**Step 4: Determine Big-O**
T(n) = n-1 = O(n)

**Step 5: Verify**
For n = 5: T(5) = 4 multiplications
- function1(value, 5) = value * function1(value, 4)  [1st multiplication]
- function1(value, 4) = value * function1(value, 3)  [2nd multiplication]
- function1(value, 3) = value * function1(value, 2)  [3rd multiplication]
- function1(value, 2) = value * function1(value, 1)  [4th multiplication]
- function1(value, 1) = value (base case)

This confirms T(5) = 4 = 5-1 ✓

**Mathematical purpose:** This function computes value^number (exponentiation).

---

### Function 2 Analysis

```python
def recursive_function2(mystring, a, b):
    if(a >= b):
        return True
    else:
        if(mystring[a] != mystring[b]):
            return False
        else:
            return recursive_function2(mystring, a+1, b-1)

def function2(mystring):
    return recursive_function2(mystring, 0, len(mystring)-1)
```

**Analysis with respect to the length of `mystring`:**

**Step 1: Identify the basic operation**
The basic operation is character comparison (`mystring[a] != mystring[b]`).

**Step 2: Set up recurrence relations**
Let n = len(mystring)
Let T2(n) = number of comparisons for function2 with string of length n
Let R(a,b) = number of comparisons for recursive_function2 with parameters a and b

For recursive_function2:
- R(a,b) = 0 if a >= b (base case)
- R(a,b) = 1 + R(a+1, b-1) if a < b (one comparison plus recursive call)

For function2:
- T2(n) = R(0, n-1)

**Step 3: Solve the recurrence**
When function2 is called with a string of length n:
- Initial call: R(0, n-1)
- The recursive calls are: R(0,n-1), R(1,n-2), R(2,n-3), ..., until a >= b

The recursion stops when a >= b:
- For even n: stops when a = n/2, b = n/2-1, so a > b
- For odd n: stops when a = (n-1)/2, b = (n-1)/2, so a = b

Number of recursive calls before base case:
- For even n: n/2 calls
- For odd n: (n+1)/2 calls

In both cases: T2(n) = ⌊n/2⌋

**Step 4: Determine Big-O**
T2(n) = ⌊n/2⌋ = O(n)

**Step 5: Verify**
For n = 6 (even): "abccba"
- R(0,5): compare 'a' and 'a' → R(1,4)
- R(1,4): compare 'b' and 'b' → R(2,3)
- R(2,3): compare 'c' and 'c' → R(3,2)
- R(3,2): a > b, return True
Total: 3 comparisons = 6/2 ✓

For n = 5 (odd): "abcba"
- R(0,4): compare 'a' and 'a' → R(1,3)
- R(1,3): compare 'b' and 'b' → R(2,2)
- R(2,2): a = b, return True
Total: 2 comparisons = ⌊5/2⌋ ✓

**Mathematical purpose:** This function checks if a string is a palindrome.


