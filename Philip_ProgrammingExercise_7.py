# This program will allow the user to enter
# a paragraph, which also includes the sentences
# beginning with a number, to display each sentence
# of that given paragraph. It will also show the total
# number of sentences that the user has given.

import re

# When the user is typing their paragraph, this code will break each
# sentence apart on a separate line depending on if they either use a
# ".", "!", or a "?". Each sentence must start off with a capital letter
# or number.
def get_sentences(s):
    pat = r'[A-Z0-9].*?[.!?](?=\s+[A-Z0-9]|$)'
    s = re.findall(pat, s, flags=re.DOTALL | re.MULTILINE)
    return s

# The program will ask the user to write a paragraph. For each sentence, it is
# separated on a specific line using the code above. Once the user finishes their
# paragraph, the program will display the results while also counting the total
# of sentences the user had written.
def main():
    print("=================================================================")
    print("Please enter a paragraph as we count each line that was inputted.")
    print("=================================================================")
    s = input("> ")

    sentences = get_sentences(s)

    print("=== Here is what you had written down: ===")
    for i in sentences:
        print('->', i)

    print(f"\nTotal of sentences the user wrote: {len(sentences)}")

main()