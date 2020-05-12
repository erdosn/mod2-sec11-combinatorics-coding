# basic structure
import numpy as np
import random
from math import factorial


def generate_data(num_points=10):
    x = [np.random.randint(0, 20) for i in range(num_points)]
    return x


def permutations(n, r):
    """
    This function takes in a total number of objects n
    and returns how many possibilities you have of listing 
    r of the n objects
    
    n: int
    r: int, r<=n
    
    return int, p number of possible permutations
    """
    return factorial(n) / factorial(n - r)


# def combinations(n, r):
#     """
#     This function takes in a total number of objects n
#     and returns how many possibilities you have of grouping 
#     r of the n objects
    
#     n: int
#     r: int, r<=n
    
#     return int, c number of possible combinations
#     """
#     if r>n:
#         print("r items chosen must be less than n items given")
#         print(f"you passed in n = {n} and r = {r}")
#         print("Don't ever do this again!!!!!!!!!")
#         return None
#     if not check_if_numerical(n):
#         print("n is not a numerical type of object\nn={n}")
#         return None
#     if not check_if_numerical(r):
#         print("r is not a numerical type of object\nr={r}")
#         return None
#     numerator = factorial(n)
#     denominator = factorial(r) * factorial(n - r)
#     return numerator / denominator


def combinations(n, r):
    """
    This function takes in a total number of objects n
    and returns how many possibilities you have of grouping 
    r of the n objects
    
    n: int
    r: int, r<=n
    
    return int, c number of possible combinations
    """
    try:
        numerator = factorial(n)
        denominator = factorial(r) * factorial(n - r)
        return numerator / denominator
    except Exception as e:
        print(f"Error was: \n{e}")
        print("combinations require that n and r are numerical types and r<=n")
        return None

    
    
def main():
    data = generate_data(num_points=50)
    print(data)
    print(len(data))
    result = combinations(10, 20)
    print(result)
    result2= combinations("this", "that")
    print(result2)


# if I run python myFunctions.py whatever is down here will run
# used for testing your file
if __name__=="__main__":
    main()