def isPrime(num):
    count = 0

    for i in range(1, num+1):
        if(i == 1 or i == num):
            continue
        if num % i == 0:
            count += 1
    if count == 0:
        return True
    else:
        return False


def run():
    num = int(input('Number: '))
    if isPrime(num):
        print(f"{num} is Prime")
    else:
        print(f"{num} is not Prime")


if __name__ == '__main__':
    run()
