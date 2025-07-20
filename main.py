# Code Setup
import sys

if len(sys.argv) > 1:
    filepath = sys.argv[1]  # Take the first argument
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)  # Default value


from stats import get_word_count
from stats import get_character_count
from stats import sort_character_count

count, file_contents = get_word_count(filepath)
character_count= get_character_count(file_contents)
sorted_chars = sort_character_count(character_count)


#Code Execution
print("============ BOOKBOT ============")
print(f"Analyzing book found at {filepath}")
print("----------- Word Count ----------")
print(f"Found {count} total words in the document")
print("--------- Character Count -------")
sorted_chars = sort_character_count(character_count)
for entry in sorted_chars:
    print(f"{entry['char']}: {entry['num']}")
print("============= END ===============")