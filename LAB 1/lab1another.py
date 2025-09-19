# Function 1: wins_rock_scissors_paper
def wins_rock_scissors_paper(player, opponent):
    player = player.lower()
    opponent = opponent.lower()
    if player == opponent:
        return False
    if (player == "rock" and opponent == "scissors") or \
       (player == "paper" and opponent == "rock") or \
       (player == "scissors" and opponent == "paper"):
        return True
    return False

# Function 2: factorial
def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Function 3: fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Function 4: sum_to_goal
def sum_to_goal(numbers, goal):
    length = len(numbers)
    for i in range(length):
        for j in range(i + 1, length):
            if numbers[i] + numbers[j] == goal:
                return numbers[i] * numbers[j]
    return 0

# UpCounter class
class UpCounter:
    def __init__(self, step=1):
        self.value = 0
        self.step = step
    def count(self):
        return self.value
    def update(self):
        self.value += self.step

# DownCounter class
class DownCounter(UpCounter):
    def update(self):
        self.value -= self.step
