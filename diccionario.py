from PyDictionary import PyDictionary

if __name__ == "__main__":
    dictionary=PyDictionary()
    word = input("Enter a word: ")
    print(word)
    meaning = dictionary.meaning(word)
    pos = 1
    for noun in meaning['Noun']:
        pos +=1
        print(f'Meaning {pos}: {noun}')