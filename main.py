
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read().lower()
    i = 0
    stringint = {}
    while i < len(file_contents): 
        singlechar = file_contents[i]
        if singlechar not in stringint:
            stringint [singlechar] = 1
        else:
            stringint [singlechar] += 1
        i += 1
    print(stringint)
main()


