# Code Functionalities
def get_word_count(filepath):
    count = 0
    with open(filepath) as f:
        file_contents = f.read()
        file_contents.split()
        for word in file_contents.split():
            count += 1
        print(f"{count} words found in the document")
        
        

def main():
    get_word_count("books/frankenstein.txt")


main()