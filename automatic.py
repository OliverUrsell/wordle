from algorithm import find_word

if __name__ == "__main__":

    final_word = "chawl"

    if len(final_word) != 5:
        raise Exception(f"The final word must be length 5: {final_word} is not")

    def automatic_input(current_word) -> str:

        print(current_word)

        output = ""

        for index, char in enumerate(current_word):
            if char == final_word[index]:
                output += "!"
            elif char in final_word:
                output += "."
            else:
                output += "x"

        return output


    current_word, guesses = find_word(automatic_input, start_word="adieu")

    print(f"\nThe correct word was: {current_word}, it took {guesses} guesses to find it.")
