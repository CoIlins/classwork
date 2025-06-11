"""
FROM WHAT WE HAVE COVERED TODAY AND WHAT WE WERE SUPPOSED TO COVER

Step1 – Define a base case:
    Identify the simplest (or base) case for
    which the solution is known or trivial.
    This is the stopping condition for the recursion,
    as it prevents the function from infinitely calling itself.

Step2 – Define a recursive case: Define the problem in terms of smaller subproblems.
    Break the problem down into smaller versions of itself,
    and call the function recursively to solve each subproblem.

Step3 – Ensure the recursion terminates:
    Make sure that the recursive function eventually reaches the base case,
    and does not enter an infinite loop.

Step4 – Combine the solutions:
    Combine the solutions of the subproblems to solve
    the original problem.
"""

def fibonacci(n):
    if n == 1:   # we return first term
        return 1
    elif n == 2:  # we return the second term
        return 1
    elif n > 2:  # we return sum of the previous two terms
        return fibonacci(n-1) + fibonacci(n-2)
for n in range(1, 4):
    print(f"{n} : {fibonacci(n)}" )

# MEMOIZATION:
# LONG
for n in range(1, 101):
    print(f"{n} : {fibonacci(n)}" )

# The cure to this is memoization
# Store the values for recent function calls
# so future calls do not have to repeat the already computed calls
# Cache values
fibonacci_cache = {}

def fibonacci_2(number):
    # A bit of type validation
    if type(number) != int:
        raise TypeError("n must be a positive int")

    if number < 1:
        raise ValueError("n must be a positive int")

    """We compute """
    # if we have cached the value then return it
    if number in fibonacci_cache:
        return fibonacci_cache[number]

    # compute the nth term
    if number == 1:
        value = 1
    elif number == 2:
        value = 1
    elif number > 2:
        value = fibonacci_2(number - 1) + fibonacci_2(number - 2)

    # Then store the computed value in our cached dictionary then return it
    fibonacci_cache[number] = value
    return value

for n in range(1, 1):
    print(n, ":", fibonacci_2(n))

# Another way to do this is to use a decoration function
# lru_cache
# L - Least. R  -> Recently. U -> Used C -> Cache
# IT PROVIDES A ONE LINE WAY TO ADD MEMOIZATION
from functools import lru_cache

@lru_cache(maxsize=1000)
def fib(n):
    if n == 1 or n == 2:
        return 1
    elif n > 2:
        return fib(n - 1) + fib(n - 2)

for n in range(1, 2099):
    print(n, ":", fib(n))

# Golden Ratio
for n in range(1 ,51):
    print(fib(n+1) / fib(n))

# SUM OF A LIST USING RECURSION
def list_sum(num_List):
    # Check if the length of the input list is 1
    if len(num_List) == 1:
        # If the list has only one element, return that element
        return num_List[0]
    else:
        # If the list has more than one element, return the sum of the first element
        # and the result of recursively calling the list_sum function on the rest of the list
        return num_List[0] + list_sum(num_List[1:])

# Print the result of calling the list_sum function with the input [2, 4, 5, 6, 7]
print(list_sum([2, 4, 5, 6, 7]))

""" 
. Sum of Nested Lists Using Recursion 
Write a Python program to sum recursion lists using recursion. 
"""
def recursive_list_sum(data_list):
    # Initialize a variable 'total' to store the cumulative sum
    total = 0

    # Iterate through each element in the input list
    for element in data_list:
        # Check if the current element is a list (nested list)
        if type(element) == type([]):
            # If the element is a list, recursively call the recursive_list_sum function on the element
            total = total + recursive_list_sum(element)
        else:
            # If the element is not a list, add its value to the total
            total = total + element

    # Return the total sum
    return total

print(recursive_list_sum([1, 2, [3, 4], [5, 6]]))

"""SUM OF HARMONIC SERIES """
# Define a function named harmonic_sum that calculates the harmonic sum up to 'n' terms
def harmonic_sum(n):
    # Check if 'n' is less than 2 (base case for the harmonic sum)
    if n < 2:
        # If 'n' is less than 2, return 1 (base case value for the harmonic sum)
        return 1
    else:
        # If 'n' is greater than or equal to 2, calculate the reciprocal of 'n'
        # and add it to the result of recursively calling the harmonic_sum function with 'n - 1'
        return 1 / n + harmonic_sum(n - 1)

# Print the result of calling the harmonic_sum function with the input value 7
print(harmonic_sum(7))

# Print the result of calling the harmonic_sum function with the input value 4
print(harmonic_sum(4))

"""LASTLY, TOWER OF HANOI"""

# Recursive Python function to solve the tower of hanoi
def TowerOfHanoi(n, source, destination_rod, auxiliary_rod):
    if n == 1:
        print("Move disk 1 from source ", source, " to destination ", destination_rod)
        return
    TowerOfHanoi(n - 1, source, auxiliary_rod, destination_rod)
    print("Move disk ", n, " from source ", source, " to destination ", destination_rod)
    TowerOfHanoi(n - 1, auxiliary_rod, destination_rod, source)

n = 4
TowerOfHanoi(n, 'A', 'B', 'C')
