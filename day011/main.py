import random
from material import logo

def blackjack_game():
    cards_info = {"A":11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}

    def draw_a_card(cards_pool):
        random.shuffle(cards_pool)
        rand_int = random.randint(1,len(cards_pool))-1
        card = cards_pool[rand_int]
        del cards_pool[rand_int]
        return card

    def cal_score(cards,cards_info = cards_info):
        score = []
        for card in cards:
            score.append(cards_info[card])
        while sum(score) > 21 and 11 in score:
            score.remove(11)
            score.append(1)
        return sum(score)
    
    def cal_win(player_cards,dealer_cards):
        if cal_score(player_cards) == cal_score(dealer_cards):
            print("It's a draw.")
        elif cal_score(player_cards) > cal_score(dealer_cards):
            print("You win!")
        else:
            print("You lose.")


    run = True
    cards_pool = list(cards_info.keys()) * 4

    player_cards = []
    dealer_cards = []
    player_cards.append(draw_a_card(cards_pool))
    player_cards.append(draw_a_card(cards_pool))
    dealer_cards.append(draw_a_card(cards_pool))
    dealer_cards.append(draw_a_card(cards_pool))

    print(logo)
    print(f"The dealer's first card is {dealer_cards[0]}")

    while run:
        print(f"Your hand is: {player_cards}.")
        hit = input("Type 'y' to get another card, type 'n' to pass: ")
        if hit == "y":
            player_cards.append(draw_a_card(cards_pool))
            if cal_score(player_cards) > 21:
                print(f"Your hand is: {player_cards}.")
                print("It's a bust, you lose.")
                run = False
        elif hit == "n":
            while cal_score(dealer_cards) <= 15:
                dealer_cards.append(draw_a_card(cards_pool))
            if cal_score(dealer_cards) > 21:
                print(f"The dealer's hand is {dealer_cards}, a total of {cal_score(dealer_cards)}.")
                print("The dealer got a bust, you win!")
            else:
                print(f"Your hand is: {player_cards}, a total of {cal_score(player_cards)}.")
                print(f"The dealer's hand is {dealer_cards}, a total of {cal_score(dealer_cards)}.")
                cal_win(player_cards,dealer_cards)
            run = False
    
    play_again = input("Do you want to play again? Type 'y' or 'n': ")
    if play_again == "y":
        blackjack_game()
    else:
        print("Goodbye.")
blackjack_game()








# print(f"Your hand is: {player_cards}, a total of {player_sum}.")
# print(f"The computer's hand is {cpu_cards}, a total of {cpu_sum}.")


# print("The computer got a bust, you win!")

# print("You lose.")

# print("You win!")

# print("It's a bust, you lose.")

# print("It's a draw.")

# print("You win!")

# print("You lose.")

# play_again = input("Do you want to play again? Type 'y' or 'n': ")

