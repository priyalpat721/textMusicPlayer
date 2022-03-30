def palindrome_checker (string):
    string = string.upper()
    string = string.replace(" ", "")

    if string[-1::-1] == string:
        return True
    return False


def main():
    word = input("What word do you want to check?")
    is_palindrome = palindrome_checker(word)
    print(is_palindrome)


if __name__ == "__main__":
    main()