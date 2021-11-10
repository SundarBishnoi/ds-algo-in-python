#Problem - Rotated Lists
#You are given list of numbers, obtained by rotating a sorted list an unknown number of times. 
# Write a function to determine the minimum number of times the original sorted list was rotated to obtain the given list. 
# Your function should have the worst-case complexity of O(log N), where N is the length of the list. 
# You can assume that all the numbers in the list are unique.
#Example: The list [5, 6, 9, 0, 2, 3, 4] was obtained by rotating the sorted list [0, 2, 3, 4, 5, 6, 9] 3 times.
#We define "rotating a list" as removing the last element of the list and adding it before the first element. 
# E.g. rotating the list [3, 2, 4, 1] produces [1, 3, 2, 4].
#"Sorted list" refers to a list where the elements are arranged in the increasing order e.g. [1, 3, 5, 7].


#----------- Optional 3 problem

def min_element(nums):
    lo, hi = 0 , len(nums)-1
    
    while lo <= hi:
        mid = (lo + hi)//2
        mid_number = nums[mid]
        
        if mid > 0 and mid_number < nums[mid-1]:
            return mid
        elif mid_number < nums[len(nums)-1]:
            lo = mid + 1
        else : 
            lo = mid-1
        
    return 0
            
            
    

def find_element_binary(nums, target):
    lo, hi = 0 , len(nums)-1
    while lo  <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            hi = mid -1
        elif nums[mid] < target:
            lo = mid + 1
    return -1
        
def find_element(nums, target):
    smallest_position =  min_element(nums)

    if smallest_position > 0:
        first_list = nums[:smallest_position]
        second_list = nums[smallest_position:]
    elif nums[smallest_position] == target:
        if len(nums) > 0:
            first_list = nums
            second_list = list()
    else : 
        print(smallest_position)
    
    if find_element_binary(first_list, target) != -1:
        return find_element_binary(first_list, target) 
    elif find_element_binary(second_list, target) != -1:
        return find_element_binary(second_list, target)
    else :
        return -1
    

    