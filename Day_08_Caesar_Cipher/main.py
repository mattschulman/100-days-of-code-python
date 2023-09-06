import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    #if the direction is 'decode' then simply make the shift a negative number so it will get
    #subtracted to get the new index
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
    #If there is a non-letter in the message, just add the non-letter to the end_text.
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    
    print(f"Here's the {cipher_direction}d result: {end_text}")

print(art.logo)

rerun = True
# Do the program in a while loop so that the user can request the alogrithm to be run again.
while rerun:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    #Validate the input
    if direction != 'encode' and direction != 'decode':
        print("You entered an invalid direction.")
        continue
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    # If the shift is greater then the size of the alphabet, use the modulus operator to return it back to under the size
    # of the alphabet 
    if shift >= len(alphabet):
        shift = shift % len(alphabet)

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    continue_choice = input('Restart the algorithm again? "yes" or "no": ').lower()
    if continue_choice == "no":
        rerun = False
