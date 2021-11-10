def locate_card(cards, query):
    pass

#Come up with some example inputs & outputs. Try to cover all edge cases

test = {
    'input': { 
        'cards': [13, 11, 10, 7, 4, 3, 1, 0], 
        'query': 7
    },
    'output': 3
}


tests = []

# query occurs in the middle
tests.append(test)

tests.append({
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 1
    },
    'output': 6
})

# query is the first element
tests.append({
    'input': {
        'cards': [4, 2, 1, -1],
        'query': 4
    },
    'output': 0
})

# query is the last element
tests.append({
    'input': {
        'cards': [3, -1, -9, -127],
        'query': -127
    },
    'output': 3
})

# cards contains just one element, query
tests.append({
    'input': {
        'cards': [6],
        'query': 6
    },
    'output': 0 
})

# cards does not contain query 
tests.append({
    'input': {
        'cards': [9, 7, 5, 2, -9],
        'query': 4
    },
    'output': -1
})

# cards is empty
tests.append({
    'input': {
        'cards': [],
        'query': 7
    },
    'output': -1
})

# numbers can repeat in cards
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 3
    },
    'output': 7
})

# query occurs multiple times
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 6
    },
    'output': 2
})

#Binary Search Algorithm 

def locate_card(cards, query):
    lo, hi = 0, len(cards)-1
    while lo <= hi:
        mid = (lo + hi) // 2
        result = test_location(cards, query, mid)

        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid-1
        elif result == 'right':
            lo = mid + 1
        
    return -1

def test_location(cards, query, mid):
    mid_number =  cards[mid]
    if mid_number == query:
        if mid-1 >= 0 and cards[mid-1] == query:
            return 'left'
        else : return 'found'
    elif mid_number < query:
        return 'left'
    elif mid_number > query:
        return 'right'

for test in tests:
    if locate_card(**test['input']) == test['output'] :
        print('Passed')
    else:
        print('Failed')