############### Blackjack Project #####################
import random
import os
from blackjackarts import logo
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards_list):
    if sum(cards_list) == 21 and len(cards_list)==2:
        return 0
    if 11 in cards_list and sum(cards_list) > 21:
        cards_list.remove(11)
        cards_list.append(1)
    return sum(cards_list)


def compare_score(user_score, computer_score):
    if user_score == computer_score:
        return "It's a draw."
    elif user_score == 0:
        return "You win with a blackjack."
    elif computer_score == 0:
        return "You lose. Opponent has a blackjack."
    elif user_score > 21:
        return "You lose. You went over 21."
    elif computer_score > 21:
        return "You win. Your opponent went over 21."
    elif user_score > computer_score:
        return "You win."
    else:
        return "You lose."

def blackjack():
    os.system("cls")
    print(logo)
    is_game_over = False
    user_cards = []
    computer_cards = []
    for i in range(0, 2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
        #user_cards += deal_card won't work here because deal card returns an integer not the list
        #computer_cards.extend(deal_card()) is same as user_cards += deal_card
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards are:{user_cards}, and Your score is: {user_score}.")
        print(f"Dealer's first card is: {computer_cards[0]}.")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Enter 'y' to draw another card, and enter 'n' to pass.\n")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True
    while computer_score != 0 and computer_score < 21:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"Your final hand is {user_cards}, and final score is {user_score}.")
    print(f"Computer's final hand is {computer_cards}, and final score is {computer_score}.")
    print(compare_score(user_score, computer_score))
    if input("Do you want to play again? Type 'y' or 'n'.\n") == "y":
        blackjack()
blackjack()

