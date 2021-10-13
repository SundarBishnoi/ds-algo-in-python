#Q (Optional): Implement a solution to the above problem using binary search.

#HINT: One way to solve this problem is to identify two sorted subarrays within the given array 
# (using the count_rotations_binary function defined above), 
# then perform a binary search on each subarray to determine the position of the target element. 
# Another way is to modify count_rotations_binary to solve the problem directly.

#----------- Optional 3 problem

def find_element(nums, target):
    pass

def count_rotation_binary(nums):
    lo, hi = 0, len(nums)-1

    while lo <= hi:
        mid = (lo + hi) // 2
        