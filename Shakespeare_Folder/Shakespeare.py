#Shakespeare
#Gets data about Shakespeare plays by building a dictionary through the iteration of a shakespeare plain text file
#Course: CS II
#Instructor: Mr. Campbell
#Date 3/17
#I pledge my Honor
#Challenges - Check if word exists in real dicitionary and Export to CSV

##import libraries
from pathlib import Path
import requests as r
from time import sleep


def validate_words(word_list):
    #Takes - word_list -- a list of tuples containing the elements, the word and the # of times it appears
    #Does - uses an http request to webscrape data off of the merriam-webster online dictionary to find out whether or not a word is real
    #     Validate_words then constructs a new list of tuples, with each tuple containing a 
    #     boolean value representing if the word is real or not
    #Returns - the list of tuples with each tuple containing the original values plus the boolean representing if the word is real
    
    for i in range(len(word_list)):
        sleep(0.25)
        url = f"https://www.merriam-webster.com/dictionary/{word_list[i][0]}"

        while True:
            try:
                req = r.get(url, timeout=2)
            except:
                pass
            break
        
        is_word = not ("Words fail us" in req.content.decode() or "The word you've entered isn't in the dictionary" in req.content.decode())
        
        word_list[i] = (word_list[i][0], word_list[i][1], is_word)
    return word_list

def get_word_data(content):
    #Takes - Content -- the full text of the Shakespeare play
    #Does - uses a for loop to iterate through the lines of the text, systematically cleaning the data and adding to a word count dictionary that 
    #       is used to track the repitions of each word in the text.
    #Returns - a sorted dictionary (greatest to lowest) of each word in the text and the number of instances of it in the text
    random_words = ["he", "to", "and", "for", "and", "nor", "thee", "thy", "but", "when", "from", "more", "third", "does", "'t", "ross", "been", "cannot",
                    "enter", "am", "my", "in", "macb.", "his", "our", "haue", "he", "be", "the", "of", "lennox", "such", "things", "up", "you.", "go",
                    "i", "a", "that", "is", "you", "with", "not", "all", "thou", "they", "it", "your", "have", "this", "what", "as", "we", "till", "him.",
                    "which", "me", "so", "do", "on", "no", "[enter", "him", "at", "by", "will", "th", "if", "yet", "shall", "upon", "her", "look", "give", "done",
                    "are", "hath", "their", "first", "was", "would", "good", "should", "like", "us", "th'", "did", "make", "or", "must", "i'll", "'tis", "let", "who", 
                    "where", "now", "how", "had", "an", "come", "them", "great", "know", "macbeth,", "say", "banquo", "duncan", "malcolm", "macbeth", "macduff", "can", "those", "most",
                    "may", "than", "scene", "=======", "second", "[they", "exit.]", "see", "were", "she", "o,", "romeo", "juliet", "then", "here", "some", "one", "exits.]"]
    
    word_count_dict = {}

    for line in content:
        for word in line.replace(".", '').replace("]", '').split():
            if word.lower() not in random_words:
                if word.lower() in word_count_dict:
                    word_count_dict[word.lower()] += 1
                else:
                    word_count_dict[word.lower()] = 1
    return sorted(word_count_dict.items(), key=lambda x:x[1], reverse = True)

def write_to_csv(data):
    #Takes -- data- a list of tuples with data including the word, repitions, and reality of the word respectively
    #Does -- iterates through the tuples, adding their values to a csv file. Each word is a new line
    #returns -- N/A
    headers = ["word", "repititions", "real"]
    
    title = input("What do you want to title your file? Hint: End with .csv:")

    with open(title, 'w') as file:
        file.write(','.join(headers) + '\n')
                
        for row in data:
            csv_row = ','.join([row[0], str(row[1]), str(row[2])])
            
            file.write(csv_row + '\n')
            
    print("Your new file has been sucessfully created!")
    
def main():
    #Takes -- N/A
    #Does -- reads in files as plain texts and then calls relevant functions for data processing based on user input
    #returns -- N/A
    try:
        current_dir = Path(__file__).parent
        file_path = current_dir / "macbeth.txt"
        macbeth = open(file_path)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        
    try:
        current_dir = Path(__file__).parent
        file_path = current_dir / "R&J.txt"
        RnJ = open(file_path)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")

    while True:
        print("1) Romeo & Juliet")
        print("2) Macbeth")
        title_choice = input("What play would you like to get the data for?")
        if title_choice == "1":
            final_dict = validate_words(get_word_data(RnJ)[:10])
            break
        elif title_choice == "2":
            final_dict = validate_words(get_word_data(macbeth)[:10])
            break
    print(final_dict)
    write_to_csv(final_dict)

main()



