def is_odd_or_even(number):
    """Desc"""
    if number % 2 == 0: print(number, " is odd")
    else: print(number, "is even")


#is_odd_or_even(10)

#is_odd_or_even(7)


def is_prime(numbers):
    """Desc"""

    for number in numbers:
        print("NUMBER", number)
        divisors = 1
        for i in range(number):
            print("DIVISORS", divisors)
            print("INDEX", i)

            if number == 1:
                print(number, "is prime")

            elif divisors == 2:
                if (i + 2) >= number:
                    print(number, "is prime")

            elif number % (i + 2) == 0:
                divisors += 1

            elif divisors > 2:
                print(number, "is not prime")




numbers = [2, 3, 4, 5, 6]
is_prime(numbers)








