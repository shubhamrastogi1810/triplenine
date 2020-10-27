import random

def main():
    
    deck = init_deck()
#    print(deck)

    play = deal(deck,10)
    for i in play:
        print(i,play[i])
#    winner = select_winner(play)


def init_deck():

    d=[('S',i) for i in range(2,15)]\
    + [('D',i) for i in range(2,15)]\
    + [('H',i) for i in range(2,15)]\
    +[('C',i) for i in range(2,15)]

    return d

def deal(d,n):
    p={}
    for i in range(1, 4) :
        for j in range(1, n+1):
            # p is a dict{playernum:[card1, card2, card3]}
            nextnum = random.randint(0, len(d))
            nextcard = d[nextnum]
            del d[nextnum]
            if j not in p:
                p[j] = [nextcard]
            else:
                p[j].append(nextcard)
    return p

if __name__=='__main__':
    main()
