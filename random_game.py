import random


def initializeGame(random_number, lifes):
    print(f"""
        {len(lifes)} opportunities assigned.
    """)
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
            lifes.pop()
            if(len(lifes)) <= 0:
                print(f"""
                💀💀GAME OVER💀💀
                The answer was {random_number}""")
                break

            if player_number < random_number:
                print(f"""
                {lifes} 
                {len(lifes)} opportunities remaining
                ⬆ Give me a higher number
                
                """)
            else:
                print(f"""
                {lifes}
                {len(lifes)} opportunities remaining
                ⬇ Give me a lower number
                
                """)


def run():
    random_number = random.randint(1, 100)
    random_lifes = random.randint(1, 10)
    lifes = ['💙']
    lifes = lifes * random_lifes

    # print(random_number)
    initializeGame(random_number, lifes)


if __name__ == '__main__':
    run()
