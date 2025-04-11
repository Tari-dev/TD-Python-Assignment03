def factorial(n: int) -> int:
    if n < 2:
        return 1
    return n * factorial(n-1)


num = int(input("Enter a number: "))
print(f"Factorial of {num} is: ", factorial(num))

