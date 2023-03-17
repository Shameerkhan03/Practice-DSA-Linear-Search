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
