import random


def prompt_number_players():
    number_of_players = input("How many players (2-8): ")
    return number_of_players


def construct_deck():
    deck = []
    for x in range(1, 14):
        for suit in ('♥', '♦', '♣', '♠'):
            deck.append(str(x)+suit)
    return deck


def players_best_hand(two_card_hand, flop, turn, river):
    def straight_flush(seven_cards):
        best_hand = None
        best_hand = "flusher"
        return best_hand

    seven_cards = two_card_hand + flop + turn + river
    five_card_hand = straight_flush(seven_cards)



def main():
    players = prompt_number_players()
    try:
        if int(players) in range(2, 9):
            pass
        else:
            print("Please input 2-8 players")
    except ValueError:
        print("Please input a number between 2-8")
        quit()
    deck = construct_deck()
    random.shuffle(deck)
    players_hands = []
    for x in range(int(players)):
        hand = (deck.pop(), deck.pop())
        players_hands.append(hand)
    for ndx, x in enumerate(players_hands):
        if ndx == 0:
            print("Your hand:", players_hands[ndx])
        else:
            print("CPU", ndx, "Hand:", players_hands[ndx])
    flop = (deck.pop(), deck.pop(), deck.pop())
    print("\nFlop:", flop)
    turn = (deck.pop(),)
    print("Turn:", turn)
    river = (deck.pop(),)
    print("River:", river)
    for hand in players_hands:
        players_best_hand(hand, flop, turn, river)


if __name__ == "__main__":
    main()