def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print("Factorial Program")
print(factorial(6))
