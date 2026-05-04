# 1. Check if a number is prime
def check_prime(n):
    if n < 2:
        print(f"{n} is not prime")
        return
    for i in range(2, n):
        if n % i == 0:
            print(f"{n} is not prime")
            return
    print(f"{n} is prime")


# 2. Find Greatest Common Divisor (Euclidean Algorithm)
def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    print(f"GCD is {a}")


# 3. Check if Even or Odd
def check_even_odd(n):
    if n % 2 == 0:
        print(f"{n} is Even")
    else:
        print(f"{n} is Odd")


# 4. Find Factorial using a loop
def find_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    print(f"Factorial is {result}")


# Usage
num = int(input("Enter number: "))
check_prime(num)
check_even_odd(num)
find_factorial(num)

val1 = int(input("Enter first number for GCD: "))
val2 = int(input("Enter second number for GCD: "))
find_gcd(val1, val2)
