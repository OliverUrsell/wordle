from algorithm import find_word
from nltk.corpus import words
import re

if __name__ == "__main__":

    word_list = [word.lower() for word in words.words() if len(word) == 5 and not re.findall('[A-Z]', word)]

    final_word = ""

    def automatic_input(current_word) -> str:

        output = ""

        for index, char in enumerate(current_word):
            if char == final_word[index]:
                output += "!"
            elif char in final_word:
                output += "."
            else:
                output += "x"

        return output

    guess_counts = dict()

    for word in word_list:
        final_word = word
        _, guesses = find_word(automatic_input, start_word="adieu")
        guess_counts[word] = guesses

        print(f"{word}: {guesses}")

    print({word: guess_counts[word] for word in guess_counts if guess_counts[word] > 6 })
