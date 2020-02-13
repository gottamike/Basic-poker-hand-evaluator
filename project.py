# -----------------------------------------+
# Michael Gotta,                           |
# CSCI 127, Program 2                      |
# Last Updated: Oct 1, 2019                |
# -----------------------------------------|
# Simplified Poker Hand evaluation system. |
# -----------------------------------------+


def get_all_ranks(hand):
    result = []
    for card in hand:
        result.append(card[0])
    return result


def royal_flush(hand):    # all the possible royal flushes in poker
    if hand == [[10, "spades"], [11, "spades"], [12, "spades"], [13, "spades"], [14, "spades"]]:
        return True
    elif hand == [[10, "diamonds"], [11, "diamonds"], [12, "diamonds"], [13, "diamonds"], [14, "diamonds"]]:
        return True
    elif hand == [[10, "clubs"], [11, "clubs"], [12, "clubs"], [13, "clubs"], [14, "clubs"]]:
        return True
    elif hand == [[10, "hearts"], [11, "hearts"], [12, "hearts"], [13, "hearts"], [14, "hearts"]]:
        return True
    else:
        return False

def straight_flush(hand):
    last_suit = None
    last = None
    for card in hand:      # loop through each card
        num = card[0]
        suit = card[1]
        if last is not None:      # how to determine a straight flush (you need the number and the symbol)
            if num - 1 != last or last_suit is not suit:
                return False
        last = num           # now they should not equal "none" and should instead hold a value
        last_suit = suit
    return True

def straight(hand):
    last = None
    for card in hand:    # loop through each card
        num = card[0]
        suit = card[1]       # suit is irrelevant
        if last is not None:    # how to determine a straight (you just need the numbers, no symbols)
            if num - 1 != last:
                return False
        last = num
    return True


def four_of_a_kind(ranks):
    if ranks[0] == ranks[1] == ranks[2] == ranks[3]:     # the program puts the cards in order so these are the only two ways to get a four of a kind
        return True
    elif ranks[4] == ranks[1] == ranks[2] == ranks[3]:
        return True
    else:
        return False



def full_house(ranks):
    if ranks[0] == ranks[1] == ranks[2] and ranks[3] == ranks[4]:      # the rest of the functions follow a similar fashion to the four_of_a_kind function
        return True
    elif ranks[4] == ranks[3] == ranks[2] and ranks[0] == ranks[1]:
        return True
    else:
        return False

def three_of_a_kind(ranks):
 if ranks[0] == ranks[1] == ranks[2]:
     return True
 elif ranks[1] == ranks[2] == ranks[3]:
     return True
 elif ranks[2] == ranks[3] == ranks[4]:
     return True
 else:
     return False

def two_pair(ranks):
    if ranks[0] == ranks[1] and ranks[2] == ranks[3]:
        return True
    elif ranks[1] == ranks[2] and ranks[3] == ranks[4]:
        return True
    elif ranks[0] == ranks[1] and ranks[3] == ranks[4]:
        return True
    else:
        return False

def one_pair(ranks):
    if ranks[0] == ranks[1]:
        return True
    elif ranks[1] == ranks[2]:
        return True
    elif ranks[2] == ranks[3]:
        return True
    elif ranks[3] == ranks[4]:
        return True
    else:
        return False

# -----------------------------------------+
# Do not modify the evaluate function.     |
# -----------------------------------------+

def evaluate(poker_hand):
    poker_hand.sort()
    poker_hand_ranks = get_all_ranks(poker_hand)
    print(poker_hand, "--> ", end="")
    if royal_flush(poker_hand):
        print("Royal Flush")
    elif straight_flush(poker_hand):
        print("Straight Flush")
    elif four_of_a_kind(poker_hand_ranks):
        print("Four of a Kind")
    elif full_house(poker_hand_ranks):
        print("Full House")
    elif straight(poker_hand):
        print("Straight")
    elif three_of_a_kind(poker_hand_ranks):
        print("Three of a Kind")
    elif two_pair(poker_hand_ranks):
        print("Two Pair")
    elif one_pair(poker_hand_ranks):
        print("One Pair")
    else:
        print("Nothing")


# -----------------------------------------+

def main():
    print("CSCI 127: Poker Hand Evaluation Program")
    print("---------------------------------------")
    evaluate([[10, "spades"], [14, "spades"], [12, "spades"], [13, "spades"], [11, "spades"]])  # royal flush
    evaluate([[10, "clubs"], [9, "clubs"], [6, "clubs"], [7, "clubs"], [8, "clubs"]])  # straight flush
    evaluate([[2, "diamonds"], [7, "clubs"], [2, "hearts"], [2, "clubs"], [2, "spades"]])  # 4 of a kind
    evaluate([[8, "diamonds"], [7, "clubs"], [8, "hearts"], [8, "clubs"], [7, "spades"]])  # full house
    evaluate([[13, "diamonds"], [7, "clubs"], [7, "hearts"], [8, "clubs"], [7, "spades"]])  # 3 of a kind
    evaluate([[10, "clubs"], [9, "clubs"], [6, "clubs"], [7, "clubs"], [8, "spades"]])  # straight
    evaluate([[10, "spades"], [9, "clubs"], [6, "diamonds"], [9, "diamonds"], [6, "hearts"]])  # 2 pair
    evaluate([[10, "spades"], [12, "clubs"], [6, "diamonds"], [9, "diamonds"], [12, "hearts"]])  # 1 pair
    evaluate([[2, "spades"], [7, "clubs"], [8, "diamonds"], [13, "diamonds"], [11, "hearts"]])  # nothing


# -----------------------------------------+

main()