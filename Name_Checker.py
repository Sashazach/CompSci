import random


vowel_counter = 0

vowels = ['a', 'i', 'o', 'u', 'y']

def name_to_word(name1):
    name = "Zachry Bostock"

    old_letter = ""
    
    for i in range(len(name1) - 1):
        scrambled_name = []
        scrambled_name.append(name[random.randint(0, len(name)-1)]) 
        
    return ''.join(scrambled_name[0:])

def zach_upper(string):
    
    upper_string = ""
    
    for char in string:
        if 122 >= ord(char) >= 97:
            upper_string += chr(ord(char) - 32)
        else:
            upper_string += char
    return upper_string

def zach_lower(string):
    
    lower_string = ""
    
    for char in string:
        if 90 >= ord(char) >= 65:
            lower_string += chr(ord(char) + 32)
        else:
            lower_string += char
            lower_string = lower_string + char
    return lower_string

elephant = input("TEST:")
print(zach_lower(elephant))
print(zach_upper(elephant))

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

print(f"Scrambled word: {name_to_word(name)}")