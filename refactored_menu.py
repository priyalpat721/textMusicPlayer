"""
    CS 5001
    Refactored menu using default arguments and flags
    Illustrates some of the Odd 'n Ends from this week's lecture
"""


def menu(message, options='123'):
    """
        Function:    menu
        Description: This function accepts a query msg and a set of
                     acceptable options as input. Returns answer from the
                     user AND a flag indicating if the answer was within
                     the acceptable options
        Params:      message - string message for user interaction
                     options (optional) - string that gives us the set of
                     allowable possibilities.
        Returns:     a Tuple. The answer and True/False depending on if user
                     choice is within the options specified
    """

    answer = input(message)
    if len(answer) == 0:
        return answer, False  # user pressed return w/o an answer
    answer = answer[0].upper()  # convert to uppercase for comparison
    if answer in options.upper():  # compare first letter if they enter more
        return answer, True
    return answer, False  # return a tuple with answer & success flag


def main():
    question = ('How do you like to keep active?\n' +
                ' 1: Running\n 2: Birdwatching\n 3: Swimming\nYour choice: ')
    answer, success = menu(question)
    print('You selected: ', answer)
    if success:
        print('We were successful in understanding your answer')
    else:
        print("Got your selection, but it's out of bounds for options")

    print()

    question = ('What if I don\'t like your default options??\n' +
                ' A: Provide your own\n B: Whatever\n C: Huh?\nYour choice: ')
    answer, success = menu(question, 'ABC')
    print('You selected: ', answer)
    if success:
        print('We were successful in understanding your 2nd answer')
    else:
        print("Got your selection, but it's out of bounds for options")


main()
