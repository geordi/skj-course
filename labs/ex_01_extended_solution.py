"""
Toto je skript pro 1. cviceni.
Doplnte kod dle pokynu cviciciho.
"""

def add(a, b):
    """Adds parameters."""
    return a + b

def what_number(number):
    """Returns string positive/zero/negative specifying
    value of the number."""
    # if <expr>:
    # elif <expr>:
    # else:
    if number > 0:
        return "positive"
    elif number == 0:
        return "zero"
    else:
        return "negative"

def fact(n):
    """Returns factorial of the n using recursion."""
    if n == 0 or n == 1:
        return 1
    else: return n*fact(n-1)

def sum_of_numbers(list_of_numbers):
    """Returns sum of the numbers in the list."""
    return sum(list_of_numbers)

def ship_name(fleet, designated_no):
    """Return ship's name for specified designated number
    from the fleet."""
    # has dictionary a key? Use syntax: key in dictionary
    if designated_no in fleet:
        return fleet[designated_no]

def dividable_by(lst, divisor):
    """Prints first integer in the lst that is
    dividable by specified divisor."""
    # types: int, float, str, list, tuble, dict
    # get type of a variable: type(variable_name)
    """
    for x in lst:
        if type(x) != int:
            continue
        if not x % divisor:
            print 'Integer dividable by %d is: %d' % (divisor, x)
            break
    """
    dividable_integer = [ x for x in lst if type(x) is int and not x % divisor ][0]
    print 'Integer dividable by %d is: %d' % (divisor, dividable_integer)

def how_many_5(numbers):
    """Returns number of numbers greater than 5."""
    # Modify example to take argument that specifies threshold
    return sum( 1 for number in numbers if number > 5 )

def gen_list_gt(lst, no):
    """Returns list with numbers greater than no."""
    #syntax: [ item for item in lst if_condition ]
    return [ item for item in lst if item > no ]

def fact_while(n):
    """Returns factorial of the n using while loop."""
    s = 1
    while n > 1:
        s *= n
        n -= 1
    return s

print(add(1, 3))
#print(add([1, 2, 3], [4, 5, 6]))
# Try addition of strings or different data type and see what happens

#if statement example
#n = 5
#print("Number", n, "is:", what_number(n))

#recursion example
#print("Factorial of number", n, "is:", fact(n))

#for example: sum of the list example
#lst = [1, 2, 3, 6, 7, 8]
#print("Sum is:", sum_of_numbers(lst))

#dictionary example
#fleet = {'BS62': 'Pegasus', "BS75": "Galactica", 36: 'Valkirie'}
#designated_no = "BS62"
#print("We've got {} in the fleet".format(ship_name(fleet, designated_no)))

#for example: find first number dividable by ...
#lst = [3, 'string1', 23, 14.0, "string2", 49, 64, 70 ]
#divisor = 8
#dividable_by(lst, divisor)

#function to count how many numbers > 5 are in the list
#lst = [1, 2, 5, 6, 7, 10, 12, 40, 3]
#print("There are {} numbers greater than 5".format(how_many_5(lst)))

#generating list example
#lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#no = 5
#print("List with numbers > {}: {}".format(no, gen_list_gt(lst, no)))

#while loop example
#print("Factorial of number", n, "is:", fact_while(n))