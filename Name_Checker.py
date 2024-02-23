import random


vowel_counter = 0

vowels = ['a', 'i', 'o', 'u', 'y']

def name_to_word(name1):
    name = "Zachry Bostock"

    old_letter = ""
    
    for i in range(len(name1) - 1):
        new_position = random.randint(0, len(name1))
        old_letter = name1[new_position]
        letter = name[i]
        name[i] = letter
        ##name1[new_position] = name[i]
        name1[i] = old_letter
    return name1

def get_first_name():
    first_name = ""
    for i in range(len(name) - 1):
        if name[i] != " ":
            first_name += name[i]
        else:
            return first_name

def get_last_name():
    last_name = ""
    for i in range(len(name) - 1, -1, -1):
        if name[i] != " ":
            last_name += name[i]
        else:
            return last_name[::-1]

def count_vowels():
    for i in range(len(name) - 1):
        if name[i].lower() in vowels:
            vowel_counter += 1

def check_hyphens():
    for i in range(len(name) - 1):
        if name[i] == "-":
            return True
    return False

name = "Zachry Bostock"

print(f"Vowels: {vowel_counter}")
print(f"Hyphen: {check_hyphens()}")

print(get_first_name())
print(get_last_name())

print(name_to_word(name))