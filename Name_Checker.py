##from zString import zString
import random
class zString:
    def __init__(self, name):
        self.name = name
        self.vowels = ['a', 'i', 'o', 'u', 'y']    

    def reverse_name(self):
        return self.name[::-1]

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
    
    def last_name(self):
        last_name = ""
        for i in range(len(self.name) - 1, -1, -1):
            if self.name[i] != " ":
                last_name += self.name[i]
            else:
                return last_name[::-1], i + 1
    
    def first_name(self):
        first_name = ""
        for i in range(len(self.name) - 1):
            if self.name[i] != " ":
                first_name += self.name[i]
            else:
                return first_name, i + 1

    def middle_name(self):
        _, first_name_end = self.first_name()
        _, last_name_start = self.last_name()
        middle_name = ""
        if len(self.Zstripped()) > len(self.first_name() + self.last_name()):
            return self.name[first_name_end:last_name_start]

    def count_vowels(self):
        for i in range(len(self.name) - 1):
            if self.name[i].lower() in self.vowels:
                vowel_counter += 1
    
nameInput = input("Please enter the name:")
name = zString(nameInput)

print(name.check_hyphen())
print(name.zach_lower())
print(name.first_name())
print(name.last_name())
print(name.middle_name())
print(name.test_middle_name())
print(name.Zstripped())

def main():
    print("Please select the check you wish to run...")
    
    print("1) Scrambe name")
    print("2) Get First Name")
    print("3) Get Middle Name")
    print("4) Get Last Name")
    print("5) Count Vowels")
    print("6) Check for Hyphens")
