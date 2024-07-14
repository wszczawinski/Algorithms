def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)


num = 6

print(f"Factorial of {num}: ", factorial(num))


def sumArr(numberArr):
    if len(numberArr) == 0:
        return 0
    else:
        return numberArr.pop() + sumArr(numberArr)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(f"Sum of {arr}: ", sumArr(arr))


def maxNumber(numberArr):
    last = numberArr.pop()
    if len(numberArr) == 1:
        return last

    previous = maxNumber(numberArr)
    if last > previous:
        return last
    else:
        return previous


arr = [7, 3, 9, 10, 3, 2, 11, 8, 5]

print(f"Biggest of {arr}: ", maxNumber(arr))
