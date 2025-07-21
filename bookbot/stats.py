# get_word_count takes a string and returns the number of words in the string by splitting
# the string by whitespace.
def get_word_count(book_text):
    words = (book_text).split()
    return len(words)

# get_letter_count takes a string and returns a dictionary with the count of each letter
# in the string, ignoring case.
def get_letter_count(book_text):
    letters = {}
    for char in(book_text):
        char = char.lower()
        if char in letters:
            letters[char] += 1
        else:
            letters[char] = 1
    return letters

def sort_list(character_count):
    sorted_character_counts = []

    # Convert the dictionary to a list of tuples (character, count)
    character_count = list(character_count.items())
    
    # Create a dictionary to hold character stats. Store the character and its count
    # Append each character and its count to a sorted_character_counts.
    for letter in character_count:
        character_stats = {} 
        character_stats["char"] = letter[0]
        character_stats["num"] = letter[1]
        sorted_character_counts.append(character_stats)

    # Sort the list of dictionaries by the 'num' key in descending order
    sorted_character_counts.sort(key=lambda x: x["num"], reverse=True)
    return sorted_character_counts