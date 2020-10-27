import random

def main():
    
    deck = init_deck()
    play = deal(deck,10)
    winner = select_winner(play)


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
            nextnum = random.randint(0, len(d)-1)
            nextcard = d[nextnum]
            del d[nextnum]
            if j not in p:
                p[j] = [nextcard]
            else:
                p[j].append(nextcard)
    return p

def select_winner(p):
    for k,v in p.items():
        v.sort(key = lambda x:x[1])
        print (k,v)
        
        if v[0][0] == v[1][0] == v[2][0]:
            print('Color:',k)

        if v[0][1] == v[1][1] == v[2][1]:
            print('Triple:',k)

        if v[0][1] == v[1][1]-1 and v[1][1] == v[2][1]-1:
            print('Series:', k)
    
    return -999

if __name__=='__main__':
    main()
