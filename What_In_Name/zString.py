import random

class zString:

    
    def __init__(self, name):
        """
        Description - A function to handle   init  .
        Takes - self, name
        Does - Performs the operation.
        Returns - Describe the return value.
        """
        self.name = name

   
    def reverse_name(self):
        """
        Description - A function to handle reverse name.
        Takes - None
        Does - reverses the name
        Returns - returns the reversed name
        """
        self = zString(self.name[::-1])
        return self
    

    
    def check_hyphen(self):
        """
        Description - A function to handle check hyphen.
        Takes - None
        Does - checks for hyphens
        Returns - returns a boolean depending on if a hyphen was found
        """
        for i in range(len(self.name) - 1):
            if self.name[i] == "-":
                return True
        return False
   
    def Zstripped(self):
     
        """
        Description - A function to handle Zstripped.
        Takes - None
        Does - strips leading whitespace from the string
        Returns - returns the stripped string
        """
        stripped_String = ""
        
        for i in range(len(self.name)):
            if self.name[i] != " ":
                stripped_String += self.name[i]

        return stripped_String
      
    
    def zach_upper(self):
        """
        Description - A function to handle zach upper.
        Takes - None
        Does - Makes the string uppercase
        Returns - returns an uppercase version of the string
        """
        upper_string = ""
        
        for char in self.name:
            if 122 >= ord(char) >= 97:
                upper_string += chr(ord(char) - 32)
            else:
                upper_string += char

        self = zString(upper_string)
        return self

    
    def zach_lower(self):
        """
        Description - A function to handle zach lower.
        Takes - None
        Does - Makes the string lowercase
        Returns - returns a lowercase version of the string
        """
        lower_string = ""
        
        for char in self.name:
            if 90 >= ord(char) >= 65:
                lower_string += chr(ord(char) + 32)
            else:
                lower_string += char

        self = zString(lower_string)
        return self
    
    
    def name_to_word(self):
        """
        Description - A function to handle name to word.
        Takes - None
        Does - scrambles letters of name into one word
        Returns - returns the scrambled word
        """
        scrambled_word = ""
        name_list = list(self.Zstripped())
        for i in range(len(self.Zstripped())): scrambled_word += name_list.pop(random.randint(0, len(name_list)-1)) 
        return scrambled_word
        
    
    def last_name(self, index=None):
        """
        Description - A function to handle last name.
        Takes - self, index=None 
        Does - gets the last name (the last word in the string)
        Returns - returns the last name
        """
        last_name = ""
        for i in range(len(self.name) - 1, -1, -1):
            if self.name[i] != " ":
                last_name += self.name[i]
            else:
                if index == None:
                    return last_name[::-1]
                return i + 1
    
    
    def first_name(self, index = None):
        """
        Description - A function to handle first name.
        Takes - self, index=None
        Does - Get the first name (first name of string)
        Returns - returns the first name
        """
        first_name = ""
        for i in range(len(self.name) - 1):
            if self.name[i] != " ":
                first_name += self.name[i]
            else:
                if index == None:
                    return first_name
                return i + 1
            
    
    def palindrome(self):
        """
        Description - A function to handle palindrome.
        Takes - None
        Does - checks if the string is a paildrome
        Returns - returns boolean depending on whether or not string is a palindrome
        """
        return self.reverse_name().zach_lower().name == self.zach_lower().name
        
    
    def middle_name(self):
        """
        Description - A function to handle middle name.
        Takes - None
        Does - checks and gets middle name (the middle words of the string)
        Returns - returns the middle name
        """
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

   
    def count_vowels(self):
        """
        Description - A function to handle count vowels.
        Takes - None
        Does - counts vowels in the string
        Returns - returns the number of vowels in the string
        """
        vowels = ['a', 'i', 'e', 'o', 'u', 'y']    
        vowel_counter = 0
        for i in range(len(self.name) - 1):
            if self.name[i].lower() in vowels:
                vowel_counter += 1
        return vowel_counter
    
    
    def has_title(self):
        """
        Description - A function to handle has title.
        Takes - None
        Does - checks if the string/name has a title
        Returns - returns boolean depending on whether string/name has a title
        """
        titles = ["Dr.", "Sir", "Esq", "Ph.d"]
        return self.first_name() in titles

    
    def consonant_frequency(self):
        """
        Description - A function to handle consonant frequency.
        Takes - None
        Does - counts consonants of the string do determine frequency
        Returns - returns dictionary containing constant frequency data
        """
        frequency_tracker = {}
        vowels = ['a', 'e', 'i', 'o', 'u', 'y']  # Added 'e' to vowels list
        for char in self.zach_lower().name:
            if char not in vowels and char.isalpha():  # Ensure char is a letter
                frequency_tracker[char] = frequency_tracker.get(char, 0) + 1
        return frequency_tracker