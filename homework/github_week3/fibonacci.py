"""
This is a Python script that takes a number as input from the
user and returns the corresponding number of Fibonacci terms.
It uses the formula for the nth term of the Fibonacci sequence
and functionally decomposes the calculations.
Fill in all the missing code in the functions and in main
"""
import typing

def get_input() -> int:
    """Gets input from the user and returns it as an integer"""
    usr_inp = int(input("Print your numb:"))
    return usr_inp


def fibonacci_list(n: int) -> typing.List[int]:
    """Returns a list of the first n Fibonacci numbers"""
    lst = []
    for i in range(n + 1):
        lst.append(fibonacci_single(i))
    return lst


def fibonacci_single(n: int) -> int:
    """Returns the nth Fibonacci number"""
    x = (golden_section_num() ** n) - (( - golden_section_reciprocal()) ** n)
    y = x / (5 ** .5)
    return y


def golden_section_num() -> float:
    """Returns the golden section number (capital Phi)"""
    pass


def golden_section_reciprocal() -> float:
    """Returns the reciprocal of the golden section number (lowercase phi)"""
    pass


def power(num: int, n: int) -> int:
    """Raises num to the nth power"""
    pass


def sqrt(num: int) -> float:
    """Returns the square root of num"""
    pass


def main():
    """Main function"""
    pass


if __name__ == "__main__":
    main()
