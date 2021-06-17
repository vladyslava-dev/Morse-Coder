from art import logo
from data import data
import sys

print(logo)
print("Welcome to Morse Coder🤓")


def translate():
    try:
        user_text = input("Enter a text for Morse code translation: ").upper()
        output_list = [data[letter] for letter in user_text]
    except KeyError:
        print("Sorry, we cannot translate some of the symbols☹️")
    else:
        output_text = "".join(output_list)
        print(f"Your text in Morse: {output_text}")
    finally:
        if_continue = input("Do you want to translate another piece of text? Print 'yes' or 'no': ").lower()
        if if_continue == "yes":
            translate()
        else:
            print("Goodbye!👋")
            sys.exit()


translate()
