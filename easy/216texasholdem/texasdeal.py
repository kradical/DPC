import random


def prompt_number_players():
    number_of_players = input("How many players (2-8): ")
    return number_of_players


def construct_deck():
    deck = []
    for x in range(1, 14):
        for suit in ('h', 'd', 'c', 's'):
            deck.append(str(x)+suit)
    return deck


def main():
    players = prompt_number_players()
    try:
        if int(players) in range(2, 9):
            pass
        else:
            print("Please input 2-8 players")
    except ValueError:
        print("Please input a number between 2-8")
    deck = construct_deck()
    random.shuffle(deck)
    players_hands = []
    for x in range(int(players)):
        hand = (deck[2*x], deck[2*x+1])
        players_hands.append(hand)
    for x in players_hands:
        print(x)


if __name__ == "__main__":
    main()