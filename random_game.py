import random


def initializeGame(random_number, random_lives):
    while True:

        player_number = 0
        try:
            player_number = int(input("Number: "))
        except:
            print("Whoops! Invalid number.")
            continue

        if(player_number == random_number):
            print(f"🎉 You won. ")
            break
        else:
            random_lives -= 1
            if(random_lives) <= 0:
                print("💀💀GAME OVER💀💀")
                break

            if player_number < random_number:
                print("💔 Wrong! Give me a higher number")
            else:
                print("💔 Wrong! Give me a lower number")


def run():
    random_number = random.randint(1, 100)
    random_lives = random.randint(1, 5)

    print(random_number)
    initializeGame(random_number, random_lives)


if __name__ == '__main__':
    run()
