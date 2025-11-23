#5.	Design a module math_utils.py with functions:
#factorial(n)
#is_prime(n)
#gcd(a,b)
#Include exception handling for invalid or negative inputs. Import and test these functions from another script.



def factorial(n):
    if not isinstance(n, int):
        raise TypeError("Factorial is only defined for integers.")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def is_prime(n):
    if not isinstance(n, int):
        raise TypeError("Prime check requires an integer.")
    if n < 0:
        raise ValueError("Prime check requires a non-negative integer.")
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):  # corrected sqrt logic
        if n % i == 0:
            return False
    return True


def gcd(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        raise TypeError("GCD requires integer inputs.")
    if a < 0 or b < 0:
        raise ValueError("GCD is not defined for negative numbers.")

    while b != 0:
        a, b = b, a % b
    return a


# ----------- Testing the functions -----------

try:
    num = int(input("Enter a number for factorial and prime check: "))
    print("Factorial:", factorial(num))
    print("Is Prime:", is_prime(num))

    a = int(input("Enter first number for GCD: "))
    b = int(input("Enter second number for GCD: "))
    print("GCD:", gcd(a, b))

except Exception as e:
    print("Error:", e)

