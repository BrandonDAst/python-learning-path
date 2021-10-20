def is_palindrome(phrase):
    # Remove spaces
    phrase = phrase.replace(" ", "")
    phrase = phrase.lower()
    reverse = phrase[::-1]
    return phrase == reverse


def run():
    phrase = input("Phrase: ")
    is_pal = is_palindrome(phrase)
    if is_pal == True:
        print(f"'{phrase}' is a palindrome. ✔")
    else:
        print(f"'{phrase}' is not a palindrome. ❌")


if __name__ == '__main__':
    run()
