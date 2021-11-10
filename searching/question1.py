#Question: Given an array of integers nums sorted in ascending order, 
# find the starting and ending position of a given number.

def first_element(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if mid > 0 and nums[mid-1] == target:
                return 'left'
            else :
                return 'found'
        elif nums[mid] < target :
            return 'right'
        else : return 'left'
    return binary_search(0, len(nums)-1, condition)

def second_element(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if mid < len(nums) and nums[mid+1] == target:
                return 'right'
            else : return 'found'
        elif nums[mid] < target :
            return 'right'
        else : return 'left'
    return binary_search(0, len(nums)-1, condition)

def binary_search(lo, hi, condition):
    while lo <= hi:
        mid = (lo+hi)//2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        elif result == 'right':
            lo = mid + 1
    return -1


first_index = first_element([1,2,3,4,5,6,8,8,19,25,29], 8)
last_index = second_element([1,2,3,4,5,6,8,8,19,25,29], 8)

print(first_index, last_index)
