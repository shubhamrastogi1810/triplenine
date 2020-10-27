import random

def main():
    
    deck = init_deck()
#    print(deck)

    play = deal(deck,10)
#    winner = select_winner(play)


def init_deck():

    d=[('S',i) for i in range(2,15)]+[('D',i) for i in range(2,15)]+[('H',i) for i in range(2,15)]+[('C',i) for i in range(2,15)]

    return d

def deal(d,n):
    p={}
    for i in range(1, 4) :
        for j in range(1, n+1):
           # p is a dict{playernum:[card1, card2, card3]}
           p[j]=d[randint(0,len(d))]

if __name__=='__main__':
    main()
