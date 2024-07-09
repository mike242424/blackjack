import random

cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
users_hand = []
house_hand = []
keep_playing = True

def add_up_score(arr):
    score = 0
    num_aces = 0
    
    for num in arr:
        if num == 'A':
            score += 11
            num_aces += 1
        elif num in ['K', 'Q', 'J']:
            score += 10
        else:
            score += int(num)
    
    while score > 21 and num_aces > 0:
        score -= 10
        num_aces -= 1
    
    return score

def deal_user_cards():
    user_card_one = random.choice(cards)
    user_card_two = random.choice(cards)
    users_hand = [user_card_one, user_card_two]
    print(f"Your cards: {users_hand}")
    return users_hand

def deal_house_cards():
    house_card_one = random.choice(cards)
    house_card_two = random.choice(cards)
    house_hand = [house_card_one, house_card_two]
    print(f"House's first card: {house_card_one}")
    return house_hand

def deal_user_card(arr):
    new_card = random.choice(cards)
    arr.append(new_card)
    return arr

def deal_house_card(arr):
    new_card = random.choice(cards)
    arr.append(new_card)
    return arr

start_game = input("Do you want to start a game of Blackjack? Type 'y' or 'n':\n")

if start_game == 'y':
    user = deal_user_cards()
    house = deal_house_cards()

    while keep_playing:
        decision = input("Type 'y' to get another card or 'n' to pass.\n")
        if decision == 'y':
            user = deal_user_card(user)
            user_score = add_up_score(user)
            print(f"Users hand: {user}")
            print(f"House's first card: {house[0]}")
            if user_score > 21:
                print(f"Users hand: {user}")
                print(f"House's hand: {house}")
                house_score = add_up_score(house)
                print(f"User has {user_score}. The house has {house_score}. You busted. The house wins.")
                keep_playing = False
        elif decision == 'n':
            house_score = add_up_score(house)
            while house_score < 17:
                house = deal_house_card(house)
                house_score = add_up_score(house)
            user_score = add_up_score(user)
            house_score = add_up_score(house)
            print(f"Users hand: {user}")
            print(f"House's hand: {house}")
            if user_score > 21:
                print(f"User has {user_score}. The house has {house_score}. You busted. The house wins.")
            elif house_score > 21:
                print(f"User has {user_score}. The house has {house_score}. The house busted. The user wins.")
            elif user_score > house_score:
                print(f"User has {user_score}. The house has {house_score}. The user wins.")
            elif house_score > user_score:
                print(f"User has {user_score}. The house has {house_score}. The house wins.")
            else:
                print(f"User has {user_score}. The house has {house_score}. It's a push.")
            keep_playing = False
