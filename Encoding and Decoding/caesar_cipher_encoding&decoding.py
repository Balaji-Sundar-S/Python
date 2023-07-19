print("""           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
""")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

again = True

while again :

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  def encrypt (plain_text, shift) :
    
    encrypted_word = ""
    for letter in plain_text :
      if letter in alphabet :
        ind = alphabet.index(letter)
        while ind + shift > 25 :
          ind -= 26
        encrypted_word += alphabet[ind + shift]
      else :
        encrypted_word += letter
    
    print (encrypted_word)
      
    
  def decrypt (plain_text, shift) :
      
    decrypted_word = ""
    for letter in plain_text :
      if letter in alphabet :
        ind = alphabet.index(letter)
        while ind - shift < 0 :
          ind += 26
        decrypted_word += alphabet[ind - shift]
      else :
        decrypted_word += letter
    
    print (decrypted_word)
      
    
  if direction == "encode" :
    encrypt(plain_text = text, shift = shift)
      
  elif direction == "decode" :
    decrypt (plain_text = text, shift = shift)
    
  else :
    print ("provide the valid option.")

  option = input ("\nwanna continue? (yes/no)\n").lower()
  if option == "yes" :
    again = True
  else :
    again = False
