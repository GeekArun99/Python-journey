import random
alphabets=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

game_on=True
def caeser(text,shift_number,encode_or_decode):
    output_text =" "
    if encode_or_decode == "decode":
        shift_number*=-1
    
    for letter in text:
        if letter not in alphabets:
            output_text +=letter
        else:   
            shift_amount= alphabets.index(letter)+shift_number
            shift_amount%=len(alphabets)
            output_text+=alphabets[shift_amount]
    print(f"here is the {encode_or_decode}d text{output_text}")

while game_on:
    text = input("enter the text you want to encrypt or decrypt : ").lower()
    shift_number=int(input("enter number of shift : "))
    encode_or_decode = input("enter encode to encrypt or decode to decrypt : ").lower()
    
    caeser(text,shift_number,encode_or_decode)

    try_again = input("You want to try again...? type yes to continue : ")
    if(try_again!="yes"):
        game_on=False  
        print("Okay then see ya..!")
        