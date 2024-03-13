# Create a list of words
words = ["Apricot", "Strawberry", "cherry", "Pineapple", "dragonfruit", "passionfruit"]

# Create a new list with words having odd number of characters using list comprehension
odd_length_words = [word for word in words if len(word) % 2 != 0]

# Print the list of words with odd number of characters
print("Words with odd number of characters:", odd_length_words)
