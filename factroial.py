def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number: "))
result = factorial(num)

print("Factorial of", num, "is", result)

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print("Factorial Program")   # NEW LINE
num = 5                      # NEW LINE
print("Factorial of", num, "is", factorial(num))  



hjhj
 # MODIFIED