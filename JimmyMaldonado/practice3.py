# Write a function area_of_circle(r) which returns the area of a circle of
# radius r only if the radius value is greater of 10.

import math
from datetime import datetime, date
import calendar

def area_of_circle(radius):
    """
    Calculates the area of a circle given a radio greater than 10
    :param radius:
    :return:
    """

    if radius > 10:
        area = math.pi * (radius**2)
        print("Area of", radius, "is:", area)
    else:
        print("Radius must be greater than 10")


area_of_circle(10)

area_of_circle(15)


# Write a function sum_to(n) that returns the sum of all integer numbers
# up to and including only until any value lower than 35. So
# sum_to(10)wouldbe1+2+3...+10which would return the value 55, but if
# n=40 only until sum to 35 need to be returned.

def sum_to(number):
    """
    Prints the sum of all integer numbers given a limit
    :param number:
    :return:
    """
    sum = 0
    for i in range(1, number + 1):
        if i < 35:
            sum += i
        else:
            print("Limit has been reached")
            break
    print("Sum of", number, "is:", sum)


sum_to(10)

sum_to(35)

sum_to(40)

# Write a function days_in_month which takes the
# name of a month, and returns the number of days in
# the month. Ignore leap years:
#
# days_in_month("February") == 28
# days_in_month("December") == 31
#
# If the function is given invalid arguments, it should
# return None.

def days_in_month(monthName):
    """
    Prints the number of days given the name of a month
    :param monthName:
    :return:
    """

    year = date.today().year
    month = datetime.strptime(monthName, '%B').month
    print(calendar.monthrange(year, month)[1])


days_in_month('January')

days_in_month('May')

days_in_month('September')
