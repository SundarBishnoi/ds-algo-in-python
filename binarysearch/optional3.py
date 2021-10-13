
nums = [8,9,10,1,2,3,4,5,6,7]
target = 7


def count_rotation_binary(nums):
    lo, hi = 0, len(nums)-1

    while lo <= hi:
        #print('lo ', lo, 'hi ', hi)
        mid = (lo + hi ) // 2 
        if mid > 0 and nums[mid] < nums[mid-1]:
            return mid
        elif nums[mid] < nums[len(nums)-1]:
            hi = mid -1
        else : lo = mid + 1

    return 0

def binary_search(lst, target):
    lo, hi = 0 , len(lst)-1
    while lo <= hi:
        mid = (lo + hi) // 2
        mid_number = lst[mid]
        #print('lo ', lo, 'hi ', hi, 'midnumber ' , mid_number)
        if mid_number == target:
            return mid
        elif mid_number > target:
            hi = mid -1
        elif mid_number < target:
            lo = mid + 1
    return -1


def find_element(nums, target):
    position = count_rotation_binary(nums)
    #print(position)
    nums1 = nums[:position]
    nums2 = nums[position:]
    result1 = binary_search(nums1, target)
    result2 = binary_search(nums2, target)
    if result1 != -1:
        #print(result)
        return result1
    elif result2 != -1:
        result2  = result2 + len(nums1)
        #print(result)
        return result2
    else : return -1    

print(find_element(nums, target))

