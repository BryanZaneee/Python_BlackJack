import random


def get_card_name(card_value):
    if card_value == 1:
        return "ACE"
    elif card_value == 11:
        return "JACK"
    elif card_value == 12:
        return "QUEEN"
    elif card_value == 13:
        return "KING"
    else:
        return str(card_value)


def print_menu():
    print("1. Get another card")
    print("2. Hold hand")
    print("3. Print statistics")
    print("4. Exit")


def play_game():
    player_hand = 0
    dealer_hand = 0
    game_number = 1
    wins = 0
    losses = 0
    ties = 0

    while True:
        print("\nSTART GAME #%d" % game_number)
        game_number += 1
        player_busted = False
        dealer_busted = False

        # Initial cards for player and dealer
        card = random.randint(1, 13)
        if card > 10:
            card = 10
        player_hand = card
        print("Your card is a %s!" % get_card_name(card))

        card = random.randint(1, 13)
        if card > 10:
            card = 10
        dealer_hand = card
        print("Dealer is showing a %s!" % get_card_name(card))

        # Player's turn
        while True:
            print("Your hand is: %d" % player_hand)
            print_menu()
            choice = int(input("Choose an option: "))
            if choice == 1:
                card = random.randint(1, 13)
                if card > 10:
                    card = 10
                player_hand += card
                print("Your card is a %s!" % get_card_name(card))
                if player_hand > 21:
                    print("You exceeded 21! You lose.")
                    losses += 1
                    player_busted = True
                    break
                elif player_hand == 21:
                    print("BLACKJACK! You win!")
                    wins += 1
                    break
            elif choice == 2:
                break
            elif choice == 3:
                print("Wins: %d" % wins)
                print("Losses: %d" % losses)
                print("Ties: %d" % ties)
            elif choice == 4:
                return

        # Dealer's turn
        if player_busted == False:
            while dealer_hand < 17:
                card = random.randint(1, 13)
                if card > 10:
                    card = 10
                dealer_hand += card

            print("Dealer's hand is %d" % dealer_hand)
            if dealer_hand > 21:
                print("Dealer busted! You win!")
                wins += 1
                dealer_busted = True
            elif dealer_hand > player_hand:
                print("Dealer wins!")
                losses += 1
            elif dealer_hand == player_hand:
                print("It's a tie!")
                ties += 1
            else:

