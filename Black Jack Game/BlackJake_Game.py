import random

def initial (deck) :

    user_list = []
    dealer_list = []
    dealer_deck = random.choice(deck)
    dealer_list.append(dealer_deck)
    for i in range (2) :

        user_deck = random.choice(deck)
        user_list.append(user_deck)

    if 11 in user_list and sum (user_list) == 21 :
        print (f"your final hand: {user_list}\tfinal score: {sum(user_list)}")
        print(f"you win :)")
        main()

    blackJake(user_list, dealer_list, deck)

def display (user_list, dealer_list) :

    print (f"your cards: {user_list}\tcurrent score: {sum(user_list)}")
    print (f"dealer's first card: {dealer_list[0]}")
    if sum(user_list) > 21 :
        print(f"you lose :(")
        main()

def blackJake (user_list, dealer_list, deck) :

    un = 2
    n = False
    while not n :
        display(user_list, dealer_list)
        user_choice = input (f"Type 'y' to get another card, type 'n' to pass : ")
        if user_choice == 'y' :
            user_list.append(random.choice(deck))
            un += 1
        else :
            n = True
    final_hand(user_list, dealer_list, deck, un)

def final_hand(user_list, dealer_list, deck, un) :

    dn = 1
    while dn < un and sum(dealer_list) < 21:
        dealer_deck = random.choice(deck)
        dealer_list.append(dealer_deck)
        dn += 1

    print (f"your final hand: {user_list}\tfinal score: {sum(user_list)}")
    print (f"dealer's final hand: {dealer_list}\tfinal score: {sum(dealer_list)}")

    if sum(dealer_list) > 21 :
            print(f"you win :)")
            main()
    elif sum(user_list) > sum(dealer_list) :
        print(f"you win :)")
    elif sum(user_list) < sum(dealer_list) :
        print(f"you lose :(")
    elif sum(user_list) == sum(dealer_list) :
        print (f"draw :|")
    
    main()

def main () :

    choice = input (f"do you want to play a game of BalckJake? type 'y' or 'n' : ")

    if choice == 'y' :
        deck = [11, 10, 10, 10, 10, 2, 3, 4, 5, 6, 7, 8, 9]
        initial(deck)
    elif choice == 'n' :
        exit()

main()