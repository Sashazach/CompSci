from pathlib import Path

def main():
    tracked_words = ["love", "hate", "fate", "death", "family", "feud", "marriage", "poison", "night", "passion", "youth", "tragedy", "verona", "honor", "loyalty"]

    try:
        current_dir = Path(__file__).parent
        file_path = current_dir / "R&J.txt"
        content = open(file_path)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")

    word_count_dict = {}
    count = 0 

    for line in content:
        for word in line.split():
            count += 1
            if word.lower() in tracked_words:
                if word in word_count_dict:
                    word_count_dict[word.lower()] += 1
                else:
                    word_count_dict[word.lower()] = 1

    print(word_count_dict)
main()

def write_to_csv(dict, data):
    headers = ["word", "repititions"]

    with open(data.csv, 'w') as file:
        file.write(','.join(headers) + '\n')
        
        for row in data:
            if row[4] == "None":
                row.insert(5, "None")
                
            csv_row = ','.join(row).replace('"', '').replace(", ", ',')
            
            file.write(csv_row + '\n')
            
    print("Your new file has been sucessfully created!")