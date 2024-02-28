import random

class zString:
    def __init__(self, name):
        self.name = name
        self.vowels = ['a', 'i', 'o', 'u', 'y']    

    def check_hyphen(self):
      for i in range(len(self.name) - 1):
        if self.name[i] == "-":
            return True
        return False
      
    def zach_upper(self):
        upper_string = ""
        
        for char in self.name:
            if 122 >= ord(char) >= 97:
                upper_string += chr(ord(char) - 32)
            else:
                upper_string += char
        return upper_string

    def zach_lower(self):
        lower_string = ""
        
        for char in self.name:
            if 90 >= ord(char) >= 65:
                lower_string += chr(ord(char) + 32)
            else:
                lower_string += char
        return lower_string
    
    def name_to_word(self):
        old_letter = ""
        
        for i in range(len(self.name) - 1):
            scrambled_name = []
            scrambled_name.append(self.name[random.randint(0, len(self.name)-1)]) 
            
        return ''.join(scrambled_name[0:])

    def first_name(self):
        first_name = ""
        for i in range(len(self.name) - 1):
            if self.name[i] != " ":
                first_name += self.name[i]
            else:
                return first_name

    def last_name(self):
        last_name = ""
        for i in range(len(self.name) - 1, -1, -1):
            if self.name[i] != " ":
                last_name += self.name[i]
            else:
                return last_name[::-1]

    def count_vowels(self):
        for i in range(len(self.name) - 1):
            if self.name[i].lower() in self.vowels:
                vowel_counter += 1