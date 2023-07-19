import random
from hangman_related import logo, stages, words_list

print(logo)

chosen_word = random.choice(words_list)

lives = 6

display = []
print ()
for i in range (len (chosen_word)-1) :
  display.append("_", )
display.append("_", )

a = True
while a:
  guess = input("Guess a letter: ").lower()

  if guess in display :
    print (f"\nYou've already guessed {guess}")

  for i in range (len(chosen_word)):
    if chosen_word[i] == guess :
      display[i] = guess
    
  if guess not in chosen_word :
    print (f"\nYou guessed {guess}, that is not in the word. You lose a life.")
    lives -= 1

  print ()
  print(display)

  print (stages[lives])
  
  if lives == 0 :
      print ("You lose.")
      print (f"The word you're trying to guess is {chosen_word}") 
      a = False
      break
    
  print ()
  
  word = ""
  for i in display :
    word += i
  
  if word == chosen_word :
    print ("\nYou Win!")
    a = False
  else :
    a = True
