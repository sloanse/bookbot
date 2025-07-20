# Code Functionalities
def get_word_count(filepath):
    count = 0
    with open(filepath) as f:
        file_contents = f.read()
        final_contents = file_contents.split()
        for word in final_contents:
            count += 1
        return count, file_contents
        
def get_character_count(file_contents):
    count = 0
    character_count = {}
    lower_final_contents = file_contents.lower()

    for character in lower_final_contents:
        if character in character_count:
            character_count[character] += 1
        else: character_count[character] = 1
        
    return character_count
               
def sort_character_count(character_count):
    char_list = []
    for char in character_count:
        entry = {"char": char, "num": character_count[char]}
        char_list.append(entry)
    def sort_on(entry):
        return entry["num"]
    char_list.sort(reverse=True, key=sort_on)
    char_final = []
    for entry in char_list:
        if str(entry["char"]).isalpha():
            char_final.append(entry)
        else:
            continue
    return char_final
