import os
#HINT: You can call clear() to clear the output in the console.

print ('''            __________
                         \                 /
                          )________(
                          |"""""""     |_.-._,.---------.,_.-._
                          |              | | |                     | | ''-.
                          |              |_| |_,---------'` '-'_| |_..-'
                          |_______| '-' `'   
                          )""""""""""""(
                         /_________\
                      /____________\
''')

a = True
dict = {}

while a :
  name = input("What's your name? : ")
  bid = int (input ("what's your bid? : $"))
  dict[name] = bid
  b = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()
  
  if b == "yes" :
    a = True
    os.system('clear')
  else :
    a = False
    
max = 0
Name = ""

for key in dict :
  if dict[key] > max :
    max = dict[key]
    Name = key
    
os.system('clear')
print (f"The winner is {Name} with a bid of ${max}.")
  
