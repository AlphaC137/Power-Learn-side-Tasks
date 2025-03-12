words = input("Enter a list of words separated by spaces: ").split()

odd_length_words = [word for word in words if len(word) % 2 != 0]

# Printing the new list
print(f"Words with an odd number of characters: {odd_length_words}")
