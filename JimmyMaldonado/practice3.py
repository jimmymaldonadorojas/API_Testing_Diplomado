# Write a function area_of_circle(r) which returns the area of a circle of
# radius r only if the radius value is greater of 10.

import math
from datetime import datetime, date


def area_of_circle(radius):
    """Calculates the area of a circle given a radio greater than 10"""

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
    """Prints the sum of all integer numbers given a limit"""
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
    """Desc"""
    currentYear = date.today().year
    print(currentYear)
    print("%s %s" % (monthName, currentYear))
    #month = datetime.strptime(monthName, '%B')
    month = datetime.strptime("%s %s" % (monthName, currentYear), '%B %Y').date()
    print(month)
    #current year
    #month as int
    #days in a month


days_in_month('January')
