from pathlib import Path
import requests as r
import time

def validate_words(word_list):
    
    for i in range(len(word_list)):
        time.sleep(0.1)
        url = f"https://www.merriam-webster.com/dictionary/{word_list[i][0]}"

        while True:
            try:
                req = r.get(url, timeout=2)
                print("14")
            except:
                print("Retrying")
            break
        
        is_word = not ("Words fail us" in req.content.decode() or "The word you've entered isn't in the dictionary" in req.content.decode())
        
        word_list[i] = (word_list[i][0], word_list[i][1], is_word)
        
    return word_list

def get_word_data(content):
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
    headers = ["word", "repititions", "real"]
    
    title = input("What do you want to title your file? Hint: End with .csv:")

    with open(title, 'w') as file:
        file.write(','.join(headers) + '\n')
                
        for row in data:
            csv_row = ','.join([row[0], str(row[1]), str(row[2])])
            
            file.write(csv_row + '\n')
            
    print("Your new file has been sucessfully created!")
    
def main():
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
            final_dict = validate_words(get_word_data(RnJ)[:])
            break
        elif title_choice == "2":
            final_dict = validate_words(get_word_data(macbeth)[:])
            break
    print(final_dict)
    write_to_csv(final_dict)
main()



