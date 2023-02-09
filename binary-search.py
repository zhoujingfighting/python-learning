#!/usr/bin/python3
"""
二分查找
"""
# element is the to be searched elemnt
def binary_search(input:list, element:int):
    start = 0
    end = len(input) - 1
    middle = 0
    while(start <= end):
        middle = (start + end) // 2
        # Compare the elemnt
        if input[middle] == element:
            print("Element is in the " + str(middle+1) + "th position")
            break
        elif input[middle] > element:
            end = middle
        else:
            if start == middle:
                start = middle + 1;
            else:
                start = middle;

binary_search([1,2,3,4,5,6,7,8], 6)
binary_search([1,2,3,4,5,6,7,8], 1)
binary_search([1,2,3,4,5,6,7,8], 8)
binary_search([1,2,3,4,5,6,7,8], 18)

