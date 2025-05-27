def wordcount(text):
    text = text.split()
    return len(text)

def charcount(text):
    counts = {}
    for char in text:
        char = char.lower()
        if char in counts:
            counts[char]+= 1
        else:
            counts[char] = 1
    return counts

def sort_chars(char_dict):
    chars_list = []
    dict_items = char_dict.items()
    dict_items=sorted(dict_items, reverse=True, key=lambda item:item[1])
    for char, count in dict_items:
        if char.isalpha():
            chars_list.append(char+": "+str(count))
    return "\n".join(chars_list)
       
       