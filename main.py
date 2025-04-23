from stats import *
import sys



def main():
    try:
        filepath = sys.argv[1]
    except IndexError:
        print("Usage: python3 main.py <path_to_book>")    
        sys.exit(1)
    count = string_to_words(filepath)
    character_count = char_count(filepath)
    sorted = sort_char(character_count)
    print("================BOOKBOT================")
    print(f"Analyzing book found at {filepath}.....")
    print("----------------Word Count-------------")
    print(f"Found {count} total words")
    print("------------Character Count------------")
    for item in sorted:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['count']}")
    print("================END====================")
   



    

if __name__ == "__main__":
    main()    

