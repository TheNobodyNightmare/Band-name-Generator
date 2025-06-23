import string
alphabet = string.ascii_lowercase
Message = True

while not Message:
  
  direction = input("Type \'encode\' to encrypt , type \'decode\' to decryt:\n " )

  text = input("Type your Message :\n ").lower()    

  shift = int(input("Enter the shift number\n"))    
      
  def encrypt(original_letter,Shift_number):
      
      cipher_text = ""
      
      for  char in original_letter:
          shifted_alphabet = alphabet.index(char) + Shift_number
          shifted_alphabet %= len(alphabet)
          cipher_text += alphabet[shifted_alphabet]            
          
      print(f"Here is the encoded code result:{cipher_text}")
      

  def decryt(orignal_letter,Shift_number):
      
      cipher_text = ""

      for char in orignal_letter:
          Reshifted_alphabet = (alphabet.index(char) - Shift_number) % 26 
          cipher_text += alphabet[Reshifted_alphabet]

      print(f"Here the decode code result:{cipher_text}") 



  if direction == "encode":
      encrypt(text,shift)
  elif direction == "decode":
        decryt(text,shift)
  else:
    print("Invalid option. Please type 'encode' or 'decode'.")      
    
  end = input("Type \'yes\' if you want to go again. Otherwise type \'no\'.")
  if end == "yes":
        Message : True
      
  if end == "no":
        Message : False
        print(" Ended")
