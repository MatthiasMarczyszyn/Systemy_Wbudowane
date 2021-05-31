import math
from typing import NoReturn

def Add(count_stack : list) -> list:
    """Simple function that add 2 last arguments on the count stack

    Parameters
    ----------
    count_stack : list
        Count stack with all of numbers from the string input

    Returns
    -------
    list
        New count stack with counted arguments
    Exapmle
    -------
    >>> Add([3,3,3])
    [3,6]
    """
    s1 = count_stack[-1]
    s2 = count_stack[-2]
    count_stack.pop()
    count_stack.pop()
    count_stack.append(s1+s2)
    return count_stack


def Multiply(count_stack : list) -> list:
    """Simple function that multiply 2 last arguments on the count stack

    Parameters
    ----------
    count_stack : list
        Count stack with all of numbers from the string input

    Returns
    -------
    list
        New count stack with counted arguments
    Exapmle
    -------
    >>> Multiply([3,3,3])
    [3,9]
    """
    s1 = count_stack[-1]
    s2 = count_stack[-2]
    count_stack.pop()
    count_stack.pop()
    count_stack.append(s1*s2)
    return count_stack

def Divide(count_stack : list) -> list:
    """Simple function that divide 2 last arguments on the count stack

    Parameters
    ----------
    count_stack : list
        Count stack with all of numbers from the string input

    Returns
    -------
    list
        New count stack with counted arguments

    Exapmle
    -------
    >>> Divide([3,3,3])
    [3,1]

    """
    s1 = count_stack[-1]
    s2 = count_stack[-2]
    count_stack.pop()
    count_stack.pop()
    count_stack.append(s2//s1)
    return count_stack

def Subtrac(count_stack : list) -> list:
    """Simple function that subtrac 2 last arguments on the count stack

    Parameters
    ----------
    count_stack : list
        Count stack with all of numbers from the string input

    Returns
    -------
    list
        New count stack with counted arguments
         Exapmle
    -------
    >>> Subtrack([3,3,3])
    [3,0]
    """
    s1 = count_stack[-1]
    s2 = count_stack[-2]
    count_stack.pop()
    count_stack.pop()
    count_stack.append(s2-s1)
    return count_stack


def RPNCalulator(expresion : str) -> int:
    """Simple function that implement RPN calculator, 
    that string data and put them to the count stack if they are numbers or make the mathematical operations.

    Parameters
    ----------
    count_stack : str
        Data input from terminal or file thats contains numers and math symbols.

    Returns
    -------
    int/bool
        Solution or Flase if syntax was wrong
     Exapmle
    -------
    >>> RPNCalculator("3,3,3++")
    9
    """
    count_stack = []
    new_number = 0
    for each in expresion:
        if each == "+":
            if new_number != 0:
                count_stack.append(new_number)
                new_number= 0
            count_stack=Add(count_stack)

        elif each == "-":
            if new_number != 0:
                count_stack.append(new_number)
                new_number= 0
            count_stack=Subtrac(count_stack)

        elif each == "*":
            if new_number != 0:
                count_stack.append(new_number)
                new_number= 0
            count_stack=Multiply(count_stack)

        elif each == "/":
            if new_number != 0:
                count_stack.append(new_number)
                new_number= 0
            count_stack=Divide(count_stack)

        elif each == ",":
            count_stack.append(new_number)
            new_number= 0

        elif each >= "0" or each <= "9":
            new_number = new_number*10 + int(each)
        
        else:
            print("Wrong syntax, try again!")
            break

    return count_stack[0]


