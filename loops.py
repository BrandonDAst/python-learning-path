def printPowerWhile(i, limit):
    base = 2
    power = 1
    result = 0
    while power <= i:
        result = base**power
        if(power == 4):  # Skip exponent 4
            power += 1
            continue

        if(result > limit):
            print("Limit reached.")
            break
        else:
            print(f"2^{power} = {result}")
            power += 1


def printPowerFor(start, end):
    for count in range(start, end+1):
        print(count)
    for i in range(10):
        print(11*i)


def printCharsWhile(phrase):
    i = 0
    while i < len(phrase):
        print(phrase[i])
        i += 1


def printCharsFor(phrase):
    for char in phrase:
        print(char)


def run():
    LIMIT = 20000
    phrase = input("Phrase: ")
    printPowerWhile(int(input("Set power: ")), LIMIT)
    # printPowerFor(1, 10)
    # printCharsWhile(phrase)
    # printCharsFor(phrase)


if __name__ == '__main__':
    run()
