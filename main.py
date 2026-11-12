import json

allowed_chars = []

# allowed_chars lisrs for languages
allowed_chars_en = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                    "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", 
                    "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", 
                    "8", "9", "0"]
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

def file_to_words(filepath="default_input.txt"):
    # turns the text file into a list of words
    newfile = open(filepath, encoding="utf-8")
    single_line = " ".join(newfile.read().splitlines()).lower()
    content = remove_banned_chars(single_line)
    # print(content)
    output = content.split(" ")
    return output

def select_language():
    selecting_language = True
    print("The selected language affects which characters are considered \"valid\" as part of a word. If your document has multiple languages, enter the language codes for every language used.")
    print("Currently usable language codes: \nen - English\nes - Spanish")

    lang = input("Language/s: ")
    if "en" in lang:
        allowed_chars += allowed_chars_en
    if "es" in lang:
        allowed_chars += allowed_chars_es
        

active = True
while active:
    words_list_unordered = []
    words_dict = {}

    select_language()

    # filepath selector
    print("You can either make a new .txt file in this folder with your text in it or you can paste your text into default_input.txt. If you paste your input into default_input, type 'n'.")
    custom_path = (input("Use a custom filepath? y/n: ")).lower()
    if custom_path == "y":
        filepath = input("Filepath: ")
        words_list_unordered = file_to_words(filepath)
    elif custom_path == "n":
        words_list_unordered = file_to_words()

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
        json.dump(desc_words, f, ensure_ascii=False, indent=4)

    done = (input("Type X to close the program")).lower()
    if input == "X":
        active = False
