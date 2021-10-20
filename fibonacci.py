def printFibonacci(postition):
    list = []
    num1 = 0
    num2 = 1
    num3 = 0

    list.append(num1)
    list.append(num2)

    for i in range(postition-1):
        num3 = num1 + num2
        list.append(num3)

        num1 = num2
        num2 = num3

    print(list)


def run():
    postition = int(input("Position: "))
    printFibonacci(postition)


if __name__ == '__main__':
    run()
