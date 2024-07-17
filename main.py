def sort_dict(dict): # Takes a dictionary and returns value of 'num' key
    return dict['num']

def main():
    file_path = "books/frankenstein.txt"
    with open(file_path) as f:
        file_contents = f.read() # Read contents of .txt file
    #print(f'Full text: {file_contents}')
    lowercase_text = file_contents.lower()
    words = lowercase_text.split() # Split massive string by whitespace
    word_count = 0
    char_count = {}
    for word in words:
        word_count += 1
        for char in word:
            if char in char_count:
                char_count[char] += 1 # Increment character count by 1
            else:
                char_count[char] = 1
    #print(f'Text word count: {word_count}')
    #print(f'Text character count: {char_count}')
    dict_list = []
    char_dict = {}
    for char in char_count: # For each char in big dictionary
        if char.isalpha(): # Take out non-letter characters
            char_dict['char'] = char 
            char_dict['num'] = char_count[char] 
            dict_list.append(char_dict) # Add new dict to a list of dictionaries
            char_dict = {} # Clear new dict
    #print(f'List of char dictionaries: {dict_list}') # Print list of dictionaries
    dict_list.sort(reverse=True, key=sort_dict) # Sorts list of dictionaries by character count
    print(f'Sorted list by char count: {dict_list}')

    print(f'////////////// Begin Report for {file_path} //////////////')
    print()
    print()
    for item in dict_list:
        print(f"The {item['char']} character was found {item['num']} times.")
    print()
    print()
    print(f'////////////// End Report for {file_path} //////////////')
    return
main()