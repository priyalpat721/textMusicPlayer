from acrostic_data import *


def print_acrostic(each):
    title = each[0]
    character = each[1]
    title_list = title.split("\n")
    message = ""

    for line in title_list:
        if line == '':
            message += " "
        else:
            message += line[character: character + 1].upper()
    print(message)


def main():
    acrostic = [[POEM, 0], [DREAM, 3]]
    for each in acrostic:
        print_acrostic(each)


if __name__ == "__main__":
    main()
