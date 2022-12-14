# Name: Christopher Boyd
# OSU Email: boydc3@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 1
# Due Date: 10/17/2022
# Description: Array Manipulation with time complexity. I'm still very weak with my pseudocode and python writing, I'm get better, but I still need a lot of extra help.


import random
from static_array import *


# ------------------- PROBLEM 1 - REVERSE -----------------------------------

def reverse(arr: StaticArray) -> None:
    """
    TODO: Write this implementation
    """
    start_index = 0

    end_index = arr.length() - 1

    while end_index > start_index:
        arr[start_index], arr[end_index] = arr[end_index], arr[start_index]
        start_index = start_index + 1
        end_index = end_index - 1


# ------------------- PROBLEM 2 - ROTATE ------------------------------------

def rotate(arr: StaticArray, steps: int) -> StaticArray:
    """
    TODO: Write this implementation
    """
    # Create a new StaticArray object - is the default size
    arr = StaticArray(arr.length())  #creates a new arr
    steps = []
    for index in range(arr):
        if steps > 0:
            rotate(arr)  + steps  #rotate right when positive int
        elif steps < 0:
            rotate(arr)  + steps  #rotate left when negative int  x + (-5) => x - 5
    return arr #rotated




# ------------------- PROBLEM 3 - SA_RANGE ----------------------------------

def sa_range(start: int, end: int) -> StaticArray:
#     """
#     TODO: Write this implementation
#     """
    # input of two integers start and end (1,6)
    # returns [1,2,3,4,5,6] in new array

    arr = StaticArray(end - start + 1)  # creates new array of x length

    for index in range(start, end):

        while index < arr.length()-1:
            if index == 0:
                # add start number to index 0

            elif index > 0 and index < arr.length() - 1:
                # shift start number to next index position.
                # add new item to former start number index.

            else:
                # last index position add end number
                # arr is ready to print

    print(arr)


#
# # ------------------- PROBLEM 4 - IS_SORTED ---------------------------------
#
def is_sorted(arr: StaticArray) -> int:
#     """
#     TODO: Write this implementation
#     """
    # receives array and returns an integer (1, -1, 0)
    # 1 if array ascending sort
    #-1 if descending sort
    # 0 otherwise
    # single element = ascending
    # set new arr.

    arr = StaticArray(test_cases)   # creates new array for the test cases

    for case in range(arr(test_cases)):
        if index  0 > 1 and 1 > arr.length-1:
            return -1
        elif index 0 < 1 and 1 < arr.legnth-1:
            return 1
        elif index 0 == (populated):
            return 1
        else:
            return 0
    return # return the return

# # ------------------- PROBLEM 5 - FIND_MODE -----------------------------------
#
def find_mode(arr: StaticArray) -> (int, int):
#     """
#     TODO: Write this implementation
#     """

    # take ascending or descending arr.
    # return mode then frequency.
    # if more than 1 high freq, select 1st
    # set new arr?

    arr = StaticArray(test_cases)    # creates new array for the test cases

    freq = 0
    for case in range(arr(test_cases)):
        if item not in arr(case):
            add item to arr

        elif item in arr(case):
             add item to arr and add item to item.temp() and freq + 1
             mode = #highest occurrence of item based on freq.
        return mode
        return freq
    return mode and freq
#
# # ------------------- PROBLEM 6 - REMOVE_DUPLICATES -------------------------
#
def remove_duplicates(arr: StaticArray) -> StaticArray:
#     """
#     TODO: Write this implementation
#     """

    # receive acending or descending array
    # return new array with duplicates removed

    arr = StaticArray(test_cases)    # creates new array for the test cases

    for case in range(arr(test_cases)):
        # search index positions for duplicates
        if item = arr(item):
            return delete item
        elif item != arr(item):
            return #add item to arr and move to next item
    return #arr sans duplicates


#
# # ------------------- PROBLEM 7 - COUNT_SORT --------------------------------
#
def count_sort(arr: StaticArray) -> StaticArray:
#     """
#     TODO: Write this implementation
#     """
    # receives array, returns new array in descending order, using count sort algarithm
    #

    arr = StaticArray(test_cases)  # creates new array for the test cases

    for case in range(arr(test_cases)):
        for index pos number in arr
            if index pos number <= new number:
                #new number added to next position
            elif index pos number >= new number:
                #move current number right one index position and insert new number in old index pos

        return #new arr


#
# # ------------------- PROBLEM 8 - SORTED SQUARES ---------------------------
#
def sorted_squares(arr: StaticArray) -> StaticArray:
#     """
#     TODO: Write this implementation
#     """
    # receive array in sorted order
    # return new array with values squared in ascending order
    #
    arr = StaticArray(test_cases)  # creates new array for the test cases

    for case in range(arr(test_cases)):
         if index_pos_number < arr.length() - 1:
        #   take index pos number ** 2 add to arr
         elif index_pos_number < arr.length() - 1:
        #    reverse(case) in new arr and run new arr back through

     return #new arr for each case with index pos number squared and arr in ascending order
        #

# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print('\n# reverse example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    reverse(arr)
    print(arr)
    reverse(arr)
    print(arr)

    print('\n# rotate example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    for steps in [1, 2, 0, -1, -2, 28, -100, 2 ** 28, -2 ** 31]:
        space = " " if steps >= 0 else ""
        print(f"{rotate(arr, steps)} {space}{steps}")
    print(arr)

    print('\n# rotate example 2')
    array_size = 1_000_000
    source = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(f'Started rotating large array of {array_size} elements')
    rotate(arr, 3 ** 14)
    rotate(arr, -3 ** 15)
    print(f'Finished rotating large array of {array_size} elements')

    print('\n# sa_range example 1')
    cases = [
        (1, 3), (-1, 2), (0, 0), (0, -3),
        (-95, -89), (-89, -95)]
    for start, end in cases:
        print(f"Start: {start: 4}, End: {end: 4}, {sa_range(start, end)}")

    print('\n# is_sorted example 1')
    test_cases = (
        [-100, -8, 0, 2, 3, 10, 20, 100],
        ['A', 'B', 'Z', 'a', 'z'],
        ['Z', 'T', 'K', 'A', '5'],
        [1, 3, -10, 20, -30, 0],
        [-10, 0, 0, 10, 20, 30],
        [100, 90, 0, -90, -200],
        ['apple']
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        result = is_sorted(arr)
        space = "  " if result and result >= 0 else " "
        print(f"Result:{space}{result}, {arr}")

    print('\n# find_mode example 1')
    test_cases = (
        [1, 20, 30, 40, 500, 500, 500],
        [2, 2, 2, 2, 1, 1, 1, 1],
        ["zebra", "sloth", "otter", "otter", "moose", "koala"],
        ["Albania", "Belgium", "Chile", "Denmark", "Egypt", "Fiji"]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value

        result = find_mode(arr)
        if result:
            print(f"{arr}\nMode: {result[0]}, Frequency: {result[1]}\n")
        else:
            print("find_mode() not yet implemented\n")

    print('# remove_duplicates example 1')
    test_cases = (
        [1], [1, 2], [1, 1, 2], [1, 20, 30, 40, 500, 500, 500],
        [5, 5, 5, 4, 4, 3, 2, 1, 1], [1, 1, 1, 1, 2, 2, 2, 2]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        print(remove_duplicates(arr))
    print(arr)

    print('\n# count_sort example 1')
    test_cases = (
        [1, 2, 4, 3, 5], [5, 4, 3, 2, 1], [0, -5, -3, -4, -2, -1, 0],
        [-3, -2, -1, 0, 1, 2, 3], [1, 2, 3, 4, 3, 2, 1, 5, 5, 2, 3, 1],
        [10100, 10721, 10320, 10998], [-100320, -100450, -100999, -100001],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        before = arr if len(case) < 50 else 'Started sorting large array'
        print(f"Before: {before}")
        result = count_sort(arr)
        after = result if len(case) < 50 else 'Finished sorting large array'
        print(f"After : {after}")

    print('\n# count_sort example 2')
    array_size = 5_000_000
    min_val = random.randint(-1_000_000_000, 1_000_000_000 - 998)
    max_val = min_val + 998
    case = [random.randint(min_val, max_val) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(case):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = count_sort(arr)
    print(f'Finished sorting large array of {array_size} elements')

    print('\n# sorted_squares example 1')
    test_cases = (
        [1, 2, 3, 4, 5],
        [-5, -4, -3, -2, -1, 0],
        [-3, -2, -2, 0, 1, 2, 3],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(sorted(case)):
            arr[i] = value
        print(arr)
        result = sorted_squares(arr)
        print(result)

    print('\n# sorted_squares example 2')
    array_size = 5_000_000
    case = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(sorted(case)):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = sorted_squares(arr)
    print(f'Finished sorting large array of {array_size} elements')
