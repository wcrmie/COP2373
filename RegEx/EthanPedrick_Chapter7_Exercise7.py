# This program allows the user to input a paragraph, whose sentences will be counted, then displayed separately.
import re


def main():

    # Immediately creates a list out of the user input.
    paragraph = split(input("Input a paragraph to have split into individual sentences."))

    print(f"\nThere were {len(paragraph)} sentences detected in the inputted paragraph.\n")

    # Loops the size of the list
    for x in range(len(paragraph)):

        # Numbers the sentence, and pops the first value.
        print(f"Sentence {x + 1}. " + f"{paragraph.pop(0)}")


def split(input):


    # Added a digit check in case the sentence started with a digit.
    pattern = r'[A-Z0-9].*?[.!?](?= [A-Z0-9]|$)'

    # Instead of creating a second variable, inlined the expression
    return re.findall(pattern, input, flags=re.DOTALL | re.MULTILINE)

main()