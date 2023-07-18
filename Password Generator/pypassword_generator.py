#Password Generator Project

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!\n")

nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password1 = ""
for i in range (nr_letters) :
  password1 += random.choice (letters)
  
password2 = ""
for i in range (nr_symbols) :
  password2 += random.choice (symbols)

password3 = ""
for i in range (nr_numbers) :
  password3 += random.choice (numbers)

password4 = ""
password4 = password1 + password2 + password3
print (f"\npassword not in randomised order of characters : {password4}\n")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password = ""
i = 0
while (i != len (password4)) :
  a = random.choice (password4)
  if a not in password :
    password += a
  else :
    i -= 1
  i += 1
print (f"password in randomised order of characters : {password}")
