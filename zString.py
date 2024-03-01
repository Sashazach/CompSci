import random

class zString:

    """
    Description - A function to handle   init  .
    Takes - self, name - Provide the necessary input(s).
    Does - Performs the operation.
    Returns - Describe the return value.
    """
    def __init__(self, name):
        self.name = name

    """
    Description - A function to handle reverse name.
    Takes - None
    Does - Performs the operation.
    Returns - Describe the return value.
    """
    def reverse_name(self):
        self = zString(self.name[::-1])
        return self
    

    """
    Description - A function to handle check hyphen.
    Takes - None
    Does - Performs the operation.
    Returns - Describe the return value.
    """
    def check_hyphen(self):
        for i in range(len(self.name) - 1):
            if self.name[i] == "-":
                return True
        return False
    
    """
    Description - A function to handle Zstripped.
    Takes - None
    Does - Performs the operation.
    Returns - Describe the return value.
    """
    def Zstripped(self):
        stripped_String = ""
        
        for i in range(len(self.name)):
            if self.name[i] != " ":
                stripped_String += self.name[i]

        return stripped_String
      
    """
    Description - A function to handle zach upper.
    Takes - None
    Does - Performs the operation.
    Returns - Describe the return value.
    """
    def zach_upper(self):
        upper_string = ""
        
        for char in self.name:
            if 122 >= ord(char) >= 97:
                upper_string += chr(ord(char) - 32)
            else:
                upper_string += char

        self = zString(upper_string)
        return self

    """
    Description - A function to handle zach lower.
    Takes - None
    Does - Performs the operation.
    Returns - Describe the return value.
    """
    def zach_lower(self):
        lower_string = ""
        
        for char in self.name:
            if 90 >= ord(char) >= 65:
                lower_string += chr(ord(char) + 32)
            else:
                lower_string += char

        self = zString(lower_string)
        return self
    
    """
    Description - A function to handle name to word.
    Takes - None
    Does - Performs the operation.
    Returns - Describe the return value.
    """
    def name_to_word(self):
        scrambled_word = ""
        name_list = list(self.Zstripped())
        for i in range(len(self.Zstripped())): scrambled_word += name_list.pop(random.randint(0, len(name_list)-1)) 
        return scrambled_word
        
    """
    Description - A function to handle last name.
    Takes - self, index=None - Provide the necessary input(s).
    Does - Performs the operation.
    Returns - Describe the return value.
    """
    def last_name(self, index=None):
        last_name = ""
        for i in range(len(self.name) - 1, -1, -1):
            if self.name[i] != " ":
                last_name += self.name[i]
            else:
                if index == None:
                    return last_name[::-1]
                return i + 1
    
    """
    Description - A function to handle first name.
    Takes - self, index=None - Provide the necessary input(s).
    Does - Performs the operation.
    Returns - Describe the return value.
    """
    def first_name(self, index = None):
        first_name = ""
        for i in range(len(self.name) - 1):
            if self.name[i] != " ":
                first_name += self.name[i]
            else:
                if index == None:
                    return first_name
                return i + 1
            
    """
    Description - A function to handle palindrome.
    Takes - None
    Does - Performs the operation.
    Returns - Describe the return value.
    """
    def palindrome(self):
        return self.reverse_name().zach_lower().name == self.zach_lower().name
        
    """
    Description - A function to handle middle name.
    Takes - None
    Does - Performs the operation.
    Returns - Describe the return value.
    """
    def middle_name(self):
        first_name_end = self.first_name(index="Index")
        last_name_start = self.last_name(index="Index")
        middle_name = ""

        try:
            if len(self.Zstripped()) > (len(self.first_name() + self.last_name())):
                self = zString(self.name[first_name_end:last_name_start])
                return self.name
            return "Middle Name Not Found"
        except:
            return "Last Name Not Found"

    """
    Description - A function to handle count vowels.
    Takes - None
    Does - Performs the operation.
    Returns - Describe the return value.
    """
    def count_vowels(self):
        vowels = ['a', 'i', 'e', 'o', 'u', 'y']    
        vowel_counter = 0
        for i in range(len(self.name) - 1):
            if self.name[i].lower() in vowels:
                vowel_counter += 1
        return vowel_counter
    
    """
    Description - A function to handle has title.
    Takes - None
    Does - Performs the operation.
    Returns - Describe the return value.
    """
    def has_title(self):
        titles = ["Dr.", "Sir", "Esq", "Ph.d"]
        return self.first_name() in titles

    """
    Description - A function to handle consonant frequency.
    Takes - None
    Does - Performs the operation.
    Returns - Describe the return value.
    """
    def consonant_frequency(self):
        frequency_tracker = {}
        vowels = ['a', 'e', 'i', 'o', 'u', 'y']  # Added 'e' to vowels list
        for char in self.zach_lower().name:
            if char not in vowels and char.isalpha():  # Ensure char is a letter
                frequency_tracker[char] = frequency_tracker.get(char, 0) + 1
        return frequency_tracker