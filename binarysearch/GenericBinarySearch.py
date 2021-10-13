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

#binary search function's job is to create search space for iterating list.
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

