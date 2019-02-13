# Create 1 script to determine is a number is
# odd or even (use single line statement if
# applies).

def is_odd_or_even(number):
    """Prints if a given number is odd or even"""

    if number % 2 == 0: print(number, " is odd")
    else: print(number, "is even")


is_odd_or_even(10)

is_odd_or_even(7)


# According a list of values between a Min and
# Max range, identify if the number is prime or
# not.

def is_prime(numbers):
    """Prints if the given numbers are primes or not"""

    for number in numbers:
        divisors = 1
        for i in range(1, number):
            if number % i == 0:
                divisors += 1

            if (i + 1) == number and divisors == 2:
                print(number, "is prime")
                break
            elif divisors > 2:
                print(number, "is not prime")
                break


numbers_1 = [2, 3, 4, 5, 7, 11, 13, 15, 17, 19, 23, 29]
is_prime(numbers_1)

numbers_2 = [5, 8, 20, 31, 33]
is_prime(numbers_2)








