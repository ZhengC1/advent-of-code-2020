numbers = []
with open("puzzle_input.txt", "rb") as f:
    numbers = [int(i) for i in f.readlines()]


TARGET = 2020
calculated = {}


def sum():
    for num in numbers:
        diff = TARGET - num
        if calculated.get(diff):
            return (diff, num)
        calculated[num] = diff


def get_multiple():
    x, y = sum()
    return x * y


print(f"dis the solution yo: {get_multiple()}")