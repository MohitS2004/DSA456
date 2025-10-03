#
#   Author: Mohit Solanki
#   This file contains recursive implementations for Lab 3
#   DSA course - Fall 2025
#   Student ID: 131874232

def factorial(number):
    """
    Returns the factorial of a number recursively.
    factorial(n) = n! = n * (n-1) * (n-2) * ... * 3 * 2 * 1
    By definition, 0! = 1
    
    Args:
        number: A non-negative integer
    
    Returns:
        The factorial of the input number
    """
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number - 1)


def linear_search(list, key):
    """
    Performs a linear search recursively to find a key in a list.
    
    Args:
        list: A list of values to search through
        key: The value to search for
    
    Returns:
        The index of the key if found, -1 if not found
    """
    return _linear_search_helper(list, key, 0)


def _linear_search_helper(list, key, index):
    """
    Helper function for recursive linear search.
    
    Args:
        list: A list of values to search through
        key: The value to search for
        index: Current index being checked
    
    Returns:
        The index of the key if found, -1 if not found
    """
    if index >= len(list):
        return -1

    if list[index] == key:
        return index

    return _linear_search_helper(list, key, index + 1)


def binary_search(list, key):
    """
    Performs a binary search recursively to find a key in a sorted list.
    
    Args:
        list: A sorted list of values to search through
        key: The value to search for
    
    Returns:
        The index of the key if found, -1 if not found
    """
    return _binary_search_helper(list, key, 0, len(list) - 1)


def _binary_search_helper(list, key, low, high):
    """
    Helper function for recursive binary search.
    
    Args:
        list: A sorted list of values to search through
        key: The value to search for
        low: Lower bound index
        high: Upper bound index
    
    Returns:
        The index of the key if found, -1 if not found
    """
    if low > high:
        return -1
    
    mid = (low + high) // 2
    
    if list[mid] == key:
        return mid
    
    elif list[mid] > key:
        return _binary_search_helper(list, key, low, mid - 1)
    
    else:
        return _binary_search_helper(list, key, mid + 1, high)