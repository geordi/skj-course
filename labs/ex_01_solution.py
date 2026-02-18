"""
Script for the first laboratory.
Add code by following instructions of the teacher.
"""

from typing import Any, List


def add(a: Any, b: Any) -> Any:
    """Adds parameters."""
    return a + b


def what_number(number: int|float) -> str:
    """Returns string positive/zero/negative specifying
    value of the number."""
    if number > 0:
        return "positive"
    elif number == 0:
        return "zero"
    else:
        return "negative"


def sum_of_numbers(list_of_numbers: List[int|float]) -> int|float:
    """Returns sum of the numbers in the list."""
    total = 0
    for n in list_of_numbers:
        total += n
    return total


def ship_name(fleet: dict, designated_no: Any) -> Any:
    """Return ship's name for specified designated number
    from the fleet."""
    # has dictionary a key? Use syntax: key in dictionary
    if designated_no in fleet:
        return fleet[designated_no]
    return None


def dividable_by(lst: List[Any], divisor: int|float) -> None:
    """Prints first integer in the lst that is
    dividable by specified divisor."""
    # types: int, float, str, list, tuble, dict
    # get type of a variable: type(variable_name)
    for item in lst:
        if type(item) == int and item % divisor == 0:
            print(item)
            return


def how_many_5(numbers: List[int|float]) -> int:
    """Returns number of numbers greater than 5."""
    # Modify example to take argument that specifies threshold
    count = 0
    for n in numbers:
        if n > 5:
            count += 1
    return count

    # OR

    return sum(1 for n in numbers if n > 5)


def gen_list_gt(lst: List[int|float], no: int|float) -> List[int|float]:
    """Returns list with numbers greater than no."""
    #syntax: [ item for item in lst if_condition ]
    return [item for item in lst if item > no]


def fact(n: int) -> int:
    """Returns factorial of n using recursion."""
    if n <= 1:
        return 1
    return n * fact(n - 1)


def fact_while(n: int) -> int:
    """Returns factorial of the n using while loop."""
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result


print(add(1, 3))
#print(add([1, 2, 3], [4, 5, 6]))
# Try addition of strings or different data type and see what happens


#if statement example
#n = 5
#print("Number", n, "is:", what_number(n))


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
#print("There are {} numbers greater than 5".format(how_many_5(lst))


#generating list example
#lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#no = 5
#print("List with numbers > {}: {}".format(no, gen_list_gt(lst, no)))


#recursion example
#print("Factorial of number", n, "is:", fact(n))


#while loop example
#print("Factorial of number", n, "is:", fact_while(n))
