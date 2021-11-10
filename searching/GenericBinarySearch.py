def locate_card(cards, query):
    #condtion function's job is to tell the direction in which we should move
    def condition(mid):
        if cards[mid] == query:
            if mid > 0 and cards[mid-1] == query:
                return 'left'
            else:
                return 'found'
        elif cards[mid] < query:
            return 'left'
        else:
            return 'right'
    
    first_index = binary_search(0, len(cards) - 1, condition)

#binary search function's job is to create search space for iterating list and this return an answer in the end..
def binary_search(lo, hi, condition):
    
    while lo <= hi:
        mid = (lo + hi) // 2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        else:
            lo = mid + 1
    return -1



# in real interview have implementation for 1 binary search problem.
# writing helper function for binary search alone can be confusing and time consuimg.
def binary_search_best(lst, target):
    lo, hi = 0 , len(lst)-1

    while lo <= hi:
        mid = ( lo + hi ) // 2
        mid_number = lst[mid]

        if mid_number == target:
             return mid
        elif mid_number < target:
            lo = mid + 1
        elif mid_number > target:
            hi = mid - 1
# if nothing is found or list is empty return `-1`
    return -1

