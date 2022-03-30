"""
   CS5001
   Fall 2020
   Priyal Patel
   Homework 5: ReMix Master functions

   A file of helper functions for remix_master
"""

from music import *

DEFAULT = PLAYLIST[0]
OPTIONS = ['L', 'T', 'S', 'P', 'R', 'X', 'Q']
MENU = "\nReMix-Master: \nL: Load a different song \n" \
       "T: Title of current song\nS: Substitute a word \n" \
       "P: Playback your song \nR: Reverse it! \n" \
       "X: Reset to original song \nQ: Quit?\nYour choice: "


def choice() -> str:
    """
    Determines if the user input for the remix menu is valid or not.
    Parameters:
        None
    Return:
        returns user input (str)
    """
    decision = input(MENU)
    decision_flag = True
    while decision_flag:
        # statement to break out of while loop
        if decision.upper() in OPTIONS:
            decision_flag = False
        else:
            # continues to take in input until acceptable
            decision = input(MENU)

    return decision.upper()


def menu(user_choice: str) -> None:
    """
    A menu for remix. Based on user input, the respective function is run
    Parameters:
        user_choice (str)
    Return:
        None
    """
    song_selection = DEFAULT
    song_lyrics = []
    while user_choice != 'Q':
        # loads song into remix player
        if user_choice == "L":
            song_selection = load()
            song_lyrics = []

        # prints out title of song
        elif user_choice == "T":
            print(("-🎵-🎶-♯🎵-" * 4) + "\nYou are mixing the song:",
                  song_selection)

        # substitutes words in songs
        elif user_choice == "S":
            song_lyrics = substitute(song_selection, song_lyrics)

        # plays songs back to user
        elif user_choice == "P":
            song_lyrics = find_song(song_selection, song_lyrics)
            print('Turn up the 808\'s and drop the beat! '
                  'Here\'s your remix:\n' + ''.join(song_lyrics) + (
                          "-🎵-🎶-♯🎵-" * 4))

        # reverses the song lyrics
        elif user_choice == "R":
            song_lyrics = reverse(song_selection, song_lyrics)

        # resets the song lyrics to original
        else:
            song_lyrics = find_song(song_selection, song_lyrics=[])
        user_choice = choice()


def load() -> str:
    """
    Loads user's choice of song from a list of options
    Parameters:
        None
    Return:
        PLAYLIST[song_selected - 1] (str)
        DEFAULT (str)
    """
    # menu of available songs
    print("\nChoose the number for song you want to load:")

    # prints number of songs with titles
    for i in range(len(PLAYLIST)):
        print(i + 1, " : ", PLAYLIST[i])

    # takes in input from user for title
    song_selected = int(input("\nYour choice: "))

    for j in range(len(PLAYLIST)):
        # if the song selected is in the playlist, it is returned
        if song_selected - 1 == j:
            return PLAYLIST[song_selected - 1]
    # returns default song if wrong selection is made
    return DEFAULT


def find_song(song_selection: str, song_lyrics: list) -> list:
    """
    Find the correct song title and returns a list of the song's lyrics
    Parameters:
        song_selection (str)
        song_lyrics (list)
    Return:
        song_lines (list)
        song_lyrics (list)
    """
    # if song lyrics is empty, list is populated with song selected lyrics
    if len(song_lyrics) == 0:
        index = 0
        song_lines = []

        for song in PLAYLIST:
            # checks if the title is in the PLAYLIST
            if song_selection == song:

                # iterates over SONGS at index
                for word in SONGS[index]:
                    song_lines += word
                    song_lines += "\n"
                return song_lines
            index += 1
    else:
        # returns song lyrics if list is not empty
        return song_lyrics


def reverse(song_selection: str, song_lyrics: list) -> list:
    """
    Reverses the lyrics of selected song
    Parameters:
        song_selection (str)
        song_lyrics (list)
    Return:
        reverse_song (list)
    """
    # selects the correct lyrics needed for modification
    song_lyrics = find_song(song_selection, song_lyrics)
    song_list = []

    song_lyrics = ''.join(song_lyrics)

    # creates a list of strings separated by \n
    song_list.append(song_lyrics.split("\n"))

    reverse_song = []
    # iterates over the list
    for sentence in song_list:
        # iterates over the string and reverses each line
        for element in sentence:
            element = element.split()
            element.reverse()
            final = ' '.join(element)
            reverse_song.append(final)
            reverse_song.append("\n")

        # removes extra \n
        reverse_song.pop()
    return reverse_song


def substitute(song_selection: str, song_lyrics: list) -> list:
    """
    Replaces a word in the song with a word given by user
    Parameters:
        song_selection (str)
        song_lyrics (list)
    Return:
        modified_song (list)
    """
    # takes in input from user to determine which word to replace
    old_word = input("What word do you want to replace in the existing song? ")
    new_word = input("What new word do you want to use for the song? ")

    # identifies the lyrics based on song title loaded
    song_lyrics = find_song(song_selection, song_lyrics)
    song_list = []

    song_lyrics = ''.join(song_lyrics)
    song_list.append(song_lyrics.split("\n"))

    modified_song = []
    # iterates over the list
    for sentence in song_list:
        # iterates over the string and replaces old word with new word
        for element in sentence:
            final = element.replace(old_word.lower(), new_word.lower())
            modified_song.append(final)
            modified_song.append("\n")

        # removes extra \n
        modified_song.pop()
    return modified_song
