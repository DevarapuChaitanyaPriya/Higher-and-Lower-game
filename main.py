from art import vs, logo
from data import data
import random
import os


def get_account():
    return random.choice(data)


def print_name(user):
    return f"{user['name']}, a {user['desc']}, from {user['country']}."


def result(user1, user2, answer):
    if (answer == 'a'
            and (user1["follower_count"] >= user2["follower_count"])):
        return score + 1
    elif (answer == 'b'
          and (user2["follower_count"] > user1["follower_count"])):
        return score + 1
    else:
        return score


score = 0
user1 = get_account()
user2 = get_account()


def display(user1, user2):
    user_1 = print_name(user1)
    user_2 = print_name(user2)
    print(f"Compare A: {user_1}")
    print()
    print(vs)
    print(f"Against B: {user_2}")


start = False
while (not start):
    print(logo)
    if (score > 0):
        print(f"You're right! Current Score: {score}")
    display(user1, user2)
    answer = input(
        "Who has more followers? Type 'A' or 'B': ").lower().rstrip()
    a = result(user1, user2, answer)
    if (a > score):
        score = a
        os.system('clear')
    else:
        start = True
        os.system('clear')
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")

    user1 = user2
    user2 = get_account()
    while user1 == user2:
        user2 = get_account()
