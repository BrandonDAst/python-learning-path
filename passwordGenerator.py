import random


def passwordGenerator():
    upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
             'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
             'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '"', '#', '$', '%', '&', '/', '(', ')', '=', '?', '¡']

    chars = upper + lower + symbols + nums

    password = []

    for n in range(15):
        random_char = random.choice(chars)
        password.append(random_char)

    password = "".join(password)

    return password


def run():
    password = passwordGenerator()
    test = password / 5
    print(test)
    print(f"Tu nueva contrasena es: {password}")


if __name__ == '__main__':
    run()
