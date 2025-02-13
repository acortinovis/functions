# TASK: Write a function that reverses a word and capitalizes it.

# Define a function that takes a string parameter
def get_reversed(word: str)->str:
    reversed_word = ""
    
    # Loop through each character in the word
    for char in word:
        # Add each character to the front of the new string (reversing it)
        reversed_word = char + reversed_word
    
    # Convert the reversed word to uppercase
    reversed_word = reversed_word.upper()
    
    # Return the final result
    return reversed_word

# Prompt the user for input
user_input = input("Please enter a word: ")

# Call the function and store the result
transformed_word = get_reversed(user_input)

# Display the transformed word
print(f"The transformed word is: {transformed_word}")