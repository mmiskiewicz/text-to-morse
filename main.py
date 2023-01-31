from morse import MORSE_CODE_DICT, ASCII_ART
import os


def morse_generator():
    print(ASCII_ART)
    text = input("Please provide some text to translate: ")
    try:
        text_translated = [MORSE_CODE_DICT[char.upper()] for char in text]
        print(''.join(text_translated))
    except KeyError as err:
        print(f"Sorry, the character you've provided {err} is not supported.")
    keep_translating = input("Would you like to continue translating? Type 'y' or 'n': ").lower()
    while keep_translating != 'n' and keep_translating != 'y':
        print("Sorry, I didn't get that.")
        keep_translating = input("Would you like to continue translating? Type 'y' or 'n': ").lower()
    if keep_translating == 'n':
        return False
    os.system('cls' if os.name == 'nt' else 'clear')
    morse_generator()


morse_generator()
