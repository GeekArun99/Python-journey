# #Password Generator Project
# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n")) 
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

# password = ""
# mixed_password =[]

# for i in range(1,nr_letters+1):
#     charecter = random.choice(letters)
#     password+=charecter
    
#     mixed_password.append(charecter)
    
# for i in range(1,nr_numbers+1):
#     charecter = random.choice(symbols)
#     password+=charecter

#     mixed_password.append(charecter)

# for i in range(1,nr_symbols+1):
#     charecter = random.choice(numbers)
#     password+=charecter

#     mixed_password.append(charecter)

# print(f"your Password is : {password}")
# random.shuffle(mixed_password)
# mx_pass=""
# for p in mixed_password:
#     mx_pass+=p

# print(f"difficult password :{mx_pass}")


#Step 1. Randomly choose a word from word list
import random

words = ["Arun", "Ricchy", "King"]
word = random.choice(words)
print(word)
lives =6

word_list = []
placeholder = " "
game_over=False

# Step 1: Create blank list
for v in word:
    word_list.append("_")

# Step 2: User input (convert both sides to same case)
while not game_over:
    ch = input("Enter a character to guess the word: ").lower()

    display=" "
    for letter in word.lower():   
        if letter == ch:
            display+=ch
            word_list.append(ch) 
        elif letter in word_list:
            display+=letter
        else:
            display+="_"
    
    if ch not in word:
        lives-=1
        if lives ==0:
            game_over=True
            print("You run out of lives, You Lost")
            print(f"the correct word is {word}")
            break
        
    print(display)
 #   print("Result:", display)
    if "_" not in display:
        game_over=True
        print("You win")


