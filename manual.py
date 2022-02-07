from algorithm import find_word

if __name__ == "__main__":
    print("""
    x - The letter is not in the word
    . - The letter is in the word but in the wrong position 
    ! - The letter is in the word in the right place
    
    """)


    def manual_input(current_word) -> str:
        input_string = input(f"Input the word {current_word} the output string is: ")
        while len(input_string) != 5:
            print("The result should only be 5 characters")
            input_string = input(f"Input the word {current_word} the output string is: ")

        return input_string


    current_word, guesses = find_word(manual_input)

    print(f"\nThe correct word was: {current_word}, it took {guesses} guesses to find it.")
