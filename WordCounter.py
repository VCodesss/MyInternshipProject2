# Importing the necessary libraries
import re

# Function to count the number of words in a string
def count_words(string):
    # Removing any non-word characters from the string
    cleaned_string = re.sub('[^a-zA-Z0-9\s]', '', string)

    # Splitting the cleaned string into individual words
    words = cleaned_string.split()

    # Returning the length of the words list
    return len(words)

# Getting user input
user_input = input("Please enter a sentence or paragraph: ")

# Checking if the input is empty
if user_input == "":
    print("Error: Empty input.")
else:
    # Counting the number of words in the input
    word_count = count_words(user_input)

    # Displaying the word count
    print("The number of words in your input is: ", word_count)