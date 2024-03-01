import random

class zString:

    def __init__(self, name):
        self.name = name

    def reverse_name(self):
        self = zString(self.name[::-1])
        return self
    

    def check_hyphen(self):
        for i in range(len(self.name) - 1):
            if self.name[i] == "-":
                return True
        return False
    
    def Zstripped(self):
        stripped_String = ""
        
        for i in range(len(self.name)):
            if self.name[i] != " ":
                stripped_String += self.name[i]

        return stripped_String
      
    def zach_upper(self):
        upper_string = ""
        
        for char in self.name:
            if 122 >= ord(char) >= 97:
                upper_string += chr(ord(char) - 32)
            else:
                upper_string += char

        self = zString(upper_string)
        return self

    def zach_lower(self):
        lower_string = ""
        
        for char in self.name:
            if 90 >= ord(char) >= 65:
                lower_string += chr(ord(char) + 32)
            else:
                lower_string += char

        self = zString(lower_string)
        return self
    
    def name_to_word(self):
        scrambled_word = ""
        name_list = list(self.Zstripped())
        for i in range(len(self.Zstripped())): scrambled_word += name_list.pop(random.randint(0, len(name_list)-1)) 
        return scrambled_word
        
    def last_name(self, index=None):
        last_name = ""
        for i in range(len(self.name) - 1, -1, -1):
            if self.name[i] != " ":
                last_name += self.name[i]
            else:
                if index == None:
                    return last_name[::-1]
                return i + 1
    
    def first_name(self, index=None):
        first_name = ""
        found_space = False
        for i in range(len(self.name)):
            # Check if the current character is not a space
            if not found_space:
                if self.name[i] != " ":
                    first_name += self.name[i]
                else:
                    found_space = True
                    if index is None:
                        break  # Exit the loop if a space is found and index is None
                    else:
                        return i + 1  # Return the position of the first space
            else:
                if index is not None:
                    return i  # Return the position after the first name if index is requested

            # Return a zString object of the first name, handling cases with no spaces
            return zString(first_name) if first_name else self
            
    def palindrome(self):
        return self.reverse_name().zach_lower().name == self.zach_lower().name
        
    def middle_name(self):
        first_name_end = self.first_name(index="Index")
        last_name_start = self.last_name(index="Index")
        middle_name = ""

        try:
            if len(self.Zstripped()) > (len(self.first_name() + self.last_name())):
                return self.name[first_name_end:last_name_start]
            return "Middle Name Not Found"
        except:
            return "Last Name Not Found"

    def count_vowels(self):
        vowels = ['a', 'i', 'e', 'o', 'u', 'y']    
        vowel_counter = 0
        for i in range(len(self.name) - 1):
            if self.name[i].lower() in self.vowels:
                vowel_counter += 1
        return vowel_counter
    
    def has_title(self):
        titles = ["Dr.", "Sir", "Esq", "Ph.d"]
        return self.first_name().Zstripped() in titles

    def consonant_frequency(self):
        frequency_tracker = {}
        vowels = ['a', 'e', 'i', 'o', 'u', 'y']  # Added 'e' to vowels list
        for char in self.zach_lower().name:
            if char not in vowels and char.isalpha():  # Ensure char is a letter
                frequency_tracker[char] = frequency_tracker.get(char, 0) + 1
        return frequency_tracker