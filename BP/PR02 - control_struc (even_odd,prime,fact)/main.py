"""def prime(num):
    if num > 1:
        for i in range(2, int(num // 2) + 1):
            if (num % i) == 0:
                print(num, "is not a prime number")
                break
        else:
            print(num, "is a prime number")
    else:
        print(num, "is not a prime number")


num = int(input("Enter a number: "))
prime(num)


def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a == b:
        return a
    if a > b:
        return gcd(a - b, b)
    return gcd(a, b - a)


a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

if gcd(a, b):
    print("GCD of", a, "and", b, "is", gcd(a, b))
else:
    print("not found")


def isEven(num):
    if num % 2 == 0:
        print(num, " is Even")
    else:
        print(num, " is Odd")


num = int(input("Enter a number: "))
isEven(num)"""


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


num = int(input("Enter a number: "))
print("Factorial of ", num, " is ", factorial(num))
