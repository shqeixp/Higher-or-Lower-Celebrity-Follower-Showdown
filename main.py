import random
from game_data import data
from art import logo, vs

def display_comparison(player_a, player_b):
    print(f"Compare A: {player_a['name']}, a {player_a['description']}, from {player_a['country']}.")
    print(vs)
    print(f"Against B: {player_b['name']}, a {player_b['description']}, from {player_b['country']}.")
    user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    return user_choice

def game():
    print("Welcome to the Higher Lower Game!")
    score = 0

    player_a = random.choice(data)
    player_b = random.choice(data)

    while True:
        while player_a == player_b:
            player_b = random.choice(data)

        print(logo)
        user_choice = display_comparison(player_a, player_b)

        if (player_a['follower_count'] > player_b['follower_count'] and user_choice == 'A') or \
           (player_a['follower_count'] < player_b['follower_count'] and user_choice == 'B'):
            score += 1
            print(f"You're right! Current score: {score}")
            player_a = player_b
            player_b = random.choice(data)
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            break

if __name__ == "__main__":
    game()
