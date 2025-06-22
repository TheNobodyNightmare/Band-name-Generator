import string
alphabet = string.ascii_lowercase
Message = False

direction = input("Type \'encode\' to encrypt , type \'decode\' to decryt:\n " )

text = input("Type your Message :\n ").lower()    

shift = int(input("Enter the shift number\n"))    
    
def encrypt(original_letter,Shift_number):
    
    cipher_text = ""
    
    for char in original_letter:
        shifted_alphabet = alphabet.index(char) + Shift_number
        cipher_text += alphabet[shifted_alphabet]            
        
    print(f"Here is the encoded code result:{cipher_text}")


encrypt(original_letter = text,Shift_number = shift)






































end = input("Type \'yes\' if you want to go again. Otherwise type \'no\'.")
if end == "yes":
    Message : False
if end == "no":
    Message : True 
    print(" Ended")     