import random

def main():
    
    deck = init_deck()
    play = deal(deck,10)
    winner = select_winner(play)
    print(winner)


def init_deck():

    d = [('S',i) for i in range(2,15)]\
    + [('D',i) for i in range(2,15)]\
    + [('H',i) for i in range(2,15)]\
    + [('C',i) for i in range(2,15)]

    return d

def deal(d,n):

    p = {}
    for i in range(1, 4) :
        for j in range(1, n+1):
            # p is a dict{playernum:[card1, card2, card3]}
            nextnum = random.randint(0, len(d)-1)
            nextcard = d[nextnum]
            del d[nextnum]
            if j not in p:
                p[j] = [nextcard]
            else:
                p[j].append(nextcard)
    return p

def select_winner(p):
    totsum = {}
    color = {}
    sequence = {}
    triple = {}

    for k,v in p.items():
        v.sort(key = lambda x:x[1]) # sort cards so its easy to find sequence
        print (k, v)

        totsum[k] = v[0][1]+v[1][1]+v[2][1] # sum total for each player if needed to decide winner
        
        if v[0][0] == v[1][0] == v[2][0]:
            color[k] = v

        if v[0][1] == v[1][1] == v[2][1]:
            triple[k] = v

        if v[0][1] == v[1][1]-1 and v[1][1] == v[2][1]-1:
            sequence[k] = v


    if triple:
        if len(triple)==1:
            return next(iter(triple))
        else:
            triple = {k: v for k, v in sorted(triple.items(), key=lambda item: item[1])}
            print("More than one triples")
            return list(triple)[-1]

    if sequence:
        if len(sequence)==1:
            return next(iter(sequence))
        else:
            sequence = {k: v for k, v in sorted(sequence.items(), key=lambda item: item[1])}
            print("More than one sequences")
            return list(sequence)[-1]

    if color:
        if len(color)==1:
            return next(iter(color))
        else:
            color = {k: v for k, v in sorted(color.items(), key=lambda item: item[1])}
            print('More than one colors')
            return list(color)[-1]

    # Sort the totsum and return the last value (which is highest)
    totsum = {k: v for k, v in sorted(totsum.items(), key=lambda item: item[1])}
    return list(totsum)[-1]

if __name__ == '__main__':
    main()
