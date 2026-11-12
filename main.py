import json

allowed_chars = []

# allowedd_chars lisrs for languages
allowed_chars_en = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                    "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", 
                    "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", 
                    "8", "9", "0"]
# TODO:; fix accented chars. For some reason they get deleted from the .json, though they don't count as banned chars. 
# Need to figure out why this happens - Fern
allowed_chars_es = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                    "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", 
                    "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", 
                    "8", "9", "0",
                    "á", "é", "í", "ó", "ú", "ñ", "ü"]

# removes any chars not in the allowed_chars list from the file
def remove_banned_chars(text):
    new_file_content = ""
    for char in text:
        if char in allowed_chars or char == " ":
            new_file_content += char
    return new_file_content

def file_to_words(filepath):
    # turns the text file into a list of words
    newfile = open(filepath)
    single_line = " ".join(newfile.read().splitlines()).lower()
    content = remove_banned_chars(single_line)
    # print(content)
    output = content.split(" ")
    return output

active = True
while active:
    selecting_language = True
    while selecting_language:
        lang = input("Language: ")

        if lang == "en":
            allowed_chars = allowed_chars_en
            selecting_language = False
        elif lang == "es":
            allowed_chars = allowed_chars_es
            selecting_language = False
        else:
            print("Invalid language selected.")

    # filepath selector
    filepath = input("Filepath: ")

    words_list_unordered = []
    words_dict = {}

    # turns the text file into a list of words
    words_list_unordered = file_to_words(filepath)

    # coutns the frequency of words
    for i in words_list_unordered:
        if i in words_dict:
            words_dict[i] = words_dict[i] + 1
        else:
            words_dict[i] = 1

    # sorts words
    desc_words = dict(sorted(words_dict.items(), key=lambda item: item[1], reverse=True))

    output_path = f"{filepath}.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(desc_words, f, indent=4)

    done = input("Type X to close the program")
    if input == "X":
        active = False
