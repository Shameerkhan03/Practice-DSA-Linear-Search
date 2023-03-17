# how to search for a specific card in a deck of multiple cards
# create a dict which has two keys. 1- inputs 2- output
# input key holds 2 more keys. 1- list of cards 2- the card we are searchng for
# output key holds the position of the card we are searching

test: dict ={
    "inputs":
    {
        "cards":[2,4,3,5,6,0],
        "query":5
    },
    "output":3
}

# before searching make a list which holds our dictionary
# in future if we want to add more dictionaries we can append the list

tests:list = []
tests.append(test)

# adding a function to search the card


def search_card(cards, query) -> int:
    position: int = 0

    while True:
        if cards[position] == query:
            return position
        
        position += 1

        if position == len(cards):
            return -1


result = (search_card(test["inputs"]["cards"], test["inputs"]["query"])) == test["output"]
print(result)

# adding more dict to the list

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