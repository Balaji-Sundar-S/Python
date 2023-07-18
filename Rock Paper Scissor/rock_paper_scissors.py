import random
a = True
while (a) :

        rock = '''
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        '''

        paper = '''
            _______
        ---'   ____)____
                  ______)
                  _______)
                 _______)
        ---.__________)
        '''

        scissors = '''
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        '''

        l = [rock, paper, scissors]
        computer_choice = random.randint(0, 2)
        user_choice = int (input ("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

        if user_choice in [0, 1, 2] :
          print (l[user_choice])
          print (f"\nComputer choice:\n{l[computer_choice]}")
          if (user_choice == computer_choice) :
            print ("Tie!")
          elif (user_choice == 0 and computer_choice == 1) :
            print ("You lose")
          elif (user_choice == 0 and computer_choice == 2) :
            print ("You win!")
          elif (user_choice == 1 and computer_choice == 0) :
            print ("You win!")
          elif (user_choice == 1 and computer_choice == 2) :
            print ("You lose")
          elif (user_choice == 2 and computer_choice == 0) :
            print ("You lose")
          elif (user_choice == 2 and computer_choice == 1) :
            print ("You win!")
            
        else :
          print ("You typed an invalid number. You lose.")

        ch = input ("\nWanna continue? (y/n)\n")
        print ()
        if ch.lower() == 'y' :
            a = True
        else :
            a = False
    
