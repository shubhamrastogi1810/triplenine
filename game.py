"""
A simple card game a la poker.

10 players. 52 cards.

Each player is dealt with 3 cards drawn randomly one-by-one to players in turn.

Cards have weights from 2-14.

select_winner will decide who wins.
"""
import secrets

def main():
    """
    The main method
    """
    deck = init_deck()
    play = deal(deck,10)
    winner = select_winner(play)
    print('Winner is {:2d}'.format(winner))


def init_deck():
    """
    Initialize the deck.
    """
    deck = [(i,'S') for i in range(2,15)]\
    + [(i, 'D') for i in range(2,15)]\
    + [(i,'H') for i in range(2,15)]\
    + [(i,'C') for i in range(2,15)]

    return deck

def deal(deck,num):
    """
    Deal the cards.
    """
    secretsGen = secrets.SystemRandom()
    play = {}
    for i in range(1, 4) :
        for j in range(1, num+1):

            # play is a dict {playernum:[card1, card2, card3]}
            nextnum = secretsGen.randint(0, len(deck)-1)
            nextcard = deck[nextnum]
            del deck[nextnum]
            if j not in play:
                play[j] = [nextcard]
            else:
                play[j].append(nextcard)
    return play

def findmax(cards):
    """
    Find maximum of the card set.
    """
    tot = {}
    for key, val in cards.items():
        tot[val[0][0] + val[1][0] + val[2][0]] = key

    return sorted(tot.items(), key=lambda x: x[0])[-1][1]


def select_winner(play):
    """
    Select the winner.
    """
    totsum = {}
    color = {}
    sequence = {}
    coloredsequence = {}
    triple = {}

    for k,val in play.items():
        val.sort(key = lambda x:x[0]) # sort cards so its easy to find sequence
        print('{:2d} {}'.format(k, val))

        # sum total for each player if needed to decide winner
        totsum[k] = val[0][0] + val[1][0] + val[2][0]

        if val[0][1] == val[1][1] == val[2][1]:
            color[k] = val

        if val[0][0] == val[1][0] == val[2][0]:
            triple[k] = val

        if val[0][0] == val[1][0]-1 and val[1][0] == val[2][0]-1:
            sequence[k] = val

        if (val[0][0] == val[1][0]-1 and val[1][0] == val[2][0]-1) and val[0][1] == val[1][1] == val[2][1]:
            coloredsequence[k] = val


    if triple:
        print('Triple')
        return findmax(triple)

    if coloredsequence:
        print('Colored Sequence')
        return findmax(coloredsequence)

    if sequence:
        print('Sequence')
        return findmax(sequence)

    if color:
        print('Color')
        return findmax(color)

    # Sort the totsum and return the last value (which is highest)
    totsum = {k: v for k, v in sorted(totsum.items(), key=lambda item: item[1])}
    print('Sum')
    return list(totsum)[-1]

if __name__ == '__main__':
    main()
