# factorial.py

num = int(input("Enter a number: "))

fact = 1

if num < 0:
    print("Factorial not possible")
else:
    for i in range(1, num + 1):
        fact = fact * i

    print("Factorial of", num, "is", fact)

    def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print("Factorial Program")
print(factorial(6))