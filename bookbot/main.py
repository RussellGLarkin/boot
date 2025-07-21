from stats import get_word_count, get_letter_count, sort_list
import sys

# get_book_text takes a filename as input, reads the file, and returns its contents as a string.
def get_book_text(filename):
    with open(filename) as f:
        file_contents = f.read()
    return file_contents

def main():
    # Check if the script is run with a filename argument
    if len(sys.argv) == 2:
        # Get the filename from the command line arguments
        filename = sys.argv[1]
        book_text = get_book_text(f'{filename}')
        word_count = get_word_count(book_text)
        character_count = get_letter_count(book_text)
        character_list = sort_list(character_count)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {filename}...")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")
        # Check if the character is an alphabetic character before printing
        for i in character_list:
            if i["char"].isalpha():
                print(f"{i['char']}: {i['num']}")
            else:
                continue
        print("============= END ===============")

    else:
        # If the script is not run with a filename argument, print usage instructions
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
main()