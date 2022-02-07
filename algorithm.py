import re
from nltk.corpus import words

def find_word(get_input_function, start_word="irate", log=False) -> (str, int):

    current_word = start_word

    word_list = [word.lower() for word in words.words() if len(word) == 5 and not re.findall('[A-Z]', word)]

    correct_word_positions = [None] * 5
    disallowed = [set(), set(), set(), set(), set()]

    input_string = ""
    banned_letters = set()
    required_letters = set()

    guesses = 0

    while input_string != "!!!!!":
        input_string = get_input_function(current_word)
        for index, character_result in enumerate(input_string):
            if character_result == "!":
                correct_word_positions[index] = current_word[index]
                required_letters.add(current_word[index])
            elif character_result == "x":
                banned_letters.add(current_word[index])
            elif character_result == ".":
                disallowed[index].add(current_word[index])
                required_letters.add(current_word[index])
            else:
                raise Exception(f"Invalid character in inputted string: {character_result} should be !, x or .")

        # Remove words that don't have letters in the right places
        for index, char in enumerate(correct_word_positions):
            if char is not None:
                word_list = [word for word in word_list if word[index] == char]

        # Remove word containing banned letters
        for banned in banned_letters:
            word_list = [word for word in word_list if banned not in word]

        # Remove words containing letters in the wrong positions
        for index, set_banned in enumerate(disallowed):
            word_list = [word for word in word_list if word[index] not in set_banned]

        # Remove words which don't contain letters we don't know the positions for yet
        for required in required_letters:
            word_list = [word for word in word_list if required in word]

        if log:
            print(f"Current correct letters and positions {correct_word_positions}")
            print(f"Current required letters {required_letters}")
            print(f"Current banned letters in positions {disallowed}")
            print(f"Current banned letters {banned_letters}")
            print(f"Possible words: {word_list}")

        guesses += 1

        current_word = word_list[0]

    return current_word, guesses
