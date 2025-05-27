import sys
from stats import wordcount
from stats import charcount
from stats import sort_chars

def get_book_text(filepath): 
    with open(filepath) as f:
        frankenstein = f.read()
    return frankenstein
def main():
    if len(sys.argv) != 2:
        print ("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    num_words = wordcount(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("----------- Character Count ----------")
    print (sort_chars(charcount(text)))
    print("----------- END ----------")
    
main()
