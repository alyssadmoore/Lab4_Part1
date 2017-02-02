import random


# should return a random number between 1 and 10
def get_random_number():
    return random.randint(1, 10)


def get_user_input():
    return int(input("Guess a number between 1 and 10.\n"))


def main():
    random_num = get_random_number()
    while True:
        guess = get_user_input()
        if guess < random_num:
            print("Higher!")
        elif guess > random_num:
            print("Lower!")
        elif guess == random_num:
            print("You win!")
            break


if __name__ == '__main__':
    main()
