import random

mydeck = [r+s for r in '23456789TJQKA' for s in 'SHDC'] 

def deal(numhands, n=5, deck=mydeck):
    # Your code here.
    shuffle(deck)
    print [deck[n*i:(i+1)*n] for i in range(numhands)]
    
def shuffle(deck):
    N = len(deck)
    for i in range(N-1):
        j = random.randrange(i,N)
        swap(deck, i, j)
    
def swap(deck, i, j):
    deck[i], deck[j] = deck[j], deck[i]

deal(5)
