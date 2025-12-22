data = [
    {"name": "Cristiano Ronaldo", "description": "Footballer", "country": "Portugal", "followers": 630},
    {"name": "Lionel Messi", "description": "Footballer", "country": "Argentina", "followers": 500},
    {"name": "Selena Gomez", "description": "Singer & Actress", "country": "USA", "followers": 430},
    {"name": "Dwayne Johnson", "description": "Actor & Wrestler", "country": "USA", "followers": 395},
    {"name": "Kylie Jenner", "description": "Entrepreneur", "country": "USA", "followers": 400},
    {"name": "Ariana Grande", "description": "Singer", "country": "USA", "followers": 380},
    {"name": "Kim Kardashian", "description": "Entrepreneur", "country": "USA", "followers": 360},
    {"name": "Virat Kohli", "description": "Cricketer", "country": "India", "followers": 270},
    {"name": "Taylor Swift", "description": "Singer", "country": "USA", "followers": 290},
    {"name": "Beyoncé", "description": "Singer", "country": "USA", "followers": 320}
]

def get_random_entry():
    import random
    return random.choice(data)
def format_entry(entry):
    name = entry["name"]
    description = entry["description"]
    country = entry["country"]
    return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'
def higher_or_lower_game(): 
    score = 0
    game_should_continue = True
    entry_a = get_random_entry()
    entry_b = get_random_entry()
    
    while entry_a == entry_b:
        entry_b = get_random_entry()
    
    while game_should_continue:
        print(f"Compare A: {format_entry(entry_a)}.")
        print("VS")
        print(f"Against B: {format_entry(entry_b)}.")
        
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        
        a_followers = entry_a["followers"]
        b_followers = entry_b["followers"]
        
        is_correct = check_answer(guess, a_followers, b_followers)
        
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
            print("-----------------------------------")
            entry_a = entry_b
            entry_b = get_random_entry()
            while entry_a == entry_b:
                entry_b = get_random_entry()
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}.")
higher_or_lower_game()
