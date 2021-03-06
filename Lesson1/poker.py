def poker(hands):
    "Return the best hand: poker([hand,...]) => hand"
    return allmax(hands, key=hand_rank)

def allmax(iterable, key=None):
    maxItem = max(iterable, key)
    return [i for i in iterable: i == maxItem]

def hand_rank(hand):
    return None

def card_ranks(hand):
    "Return a list of the ranks, sorted with higher first."
    ranks = ['--23456789TJQKA'.index(r) for r,s in hand]
    ranks.sort(reverse=True)
    return ranks

def kind(n, ranks):
    """Return the first rank that this hand has exactly n of.
        Return None if there is no n-of-a-kind in the hand."""
    # Your code here.
    for r in ranks:
        if ranks.count(r) == n:
            return r
    return None

def straight(ranks):
    "Return True if the ordered ranks form a 5-card straight."
    # Your code here.
    return (max(ranks) - min(ranks) == 4) & (len(set(ranks)) == 5)

def flush(hand):
    "Return True if all the cards have the same suit."
    # Your code here.
    suits = [s for r,s in hand]
    return len(set(suits)) == 1

def test():
    "Test cases for the functions in poker program"
    sf = "6C 7C 8C 9C TC".split() # => ['6C', '7C', '8C', '9C', 'TC']
    fk = "9D 9H 9S 9C 7D".split() 
    fh = "TD TC TH 7C 7D".split()
    assert poker([sf, fk, fh]) == sf
    assert poker([fk, fh]) == fk
    assert poker([fh, fh]) == fh
    assert poker([sf]) == sf
    assert poker([sf] * 100) == sf
    return 'tests pass'

print test()
