import random
#____________________________________________________________________________________
#Get 2 cards for each player 1.Computer 2.User  
def deal_card(list):
    for r in range(2):
        card=random.choice(cards)
        list.append(card)
#____________________________________________________________________________________
#Check for BlackJack or bust
def blackjack():
    user_sum=sum(user_cards)
    computer_sum=sum(Computer_cards)
    print(f"Your cards: {user_cards}, current score: {user_sum}")
    print(f"Computer's first card: {Computer_cards[0]}")

    if user_sum==21:
        game_over=True
        print("Win with a Blackjack")
    elif computer_sum==21:
        game_over=True
        print("Lose, opponent has Blackjack")
    elif user_sum>21:
        calculate_score(user_cards)
        calculate_score(Computer_cards)
    else:
        print("Game continues")
#___________________________________________________________________________________
 #   Check score is more than 21 and ace is one of the card in the list 
def calculate_score(list):
    if 11 in list and sum(list)>21:
        list.remove(11)
        list.append(1)
        print(f"list items :{list} and Sum : {sum(list)}")
    elif sum(list)>21 and 11 not in list:
        game_over=True
        print("You went over. You lose")

#___________________________________________________________________________________
    #Ask for 3rd Card
def user_choice():
    user_sum=sum(user_cards)
    if user_sum<21:
        choice=input("Type 'y' to get another card, type 'n' to pass: ")
        if choice=='y':
            card=random.choice(cards)
            user_cards.append(card)
            print(f"user_cards : {user_cards}")
        else:
            print(f"user_cards : {user_cards}")
    else:
        print(f"user_cards : {user_cards}")
#_______________________________________________________________________________________
    #Computer sum is less than 17 then ask for another card   

def computer_choice():
    computer_sum=sum(Computer_cards)
    while computer_sum<17:
        card=random.choice(cards)
        Computer_cards.append(card)
        computer_sum=sum(Computer_cards)
    print(f"Computer cards :{Computer_cards}")
    return Computer_cards

#Compare scores and declare winner

def compare(user_sum,computer_sum):
    if user_sum>21:
        game_over=True
        print("You went over. You lose")
    elif computer_sum>21:
        game_over=True
        print("Opponent went over. You win")
    elif user_sum==computer_sum:
        game_over=True
        print("It's a Draw")
    elif user_sum>computer_sum:
        game_over=True
        print("You win")
    else:
        game_over=True
        print("You lose")

#------------------------------------------------------------------------------------------
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
user_cards=[]
Computer_cards=[]
def BlackJack():
    game_over=False
    while not game_over:
        deal_card(user_cards)
        deal_card(Computer_cards)
        blackjack()
        user_choice()
        computer_choice()
        compare(sum(user_cards),sum(Computer_cards))
        game_over=True

BlackJack()
game_continue=True
while game_continue:
    play_again=input("Do you want to play again....? Type 'y' or 'n': ").lower()
    if play_again=='y':
        user_cards=[]
        Computer_cards=[]
        BlackJack()
    else:
        print("Thank you for playing")



    



