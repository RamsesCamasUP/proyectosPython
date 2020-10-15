from PyDictionary import PyDictionary

if __name__ == "__main__":
    dictionary=PyDictionary()
    word = input("Enter a word: ")
    meaning = dictionary.meaning(word)
    pos = 0
    for noun in meaning['Verb']:
        pos +=1
        print(f'Meaning {pos}: {noun}')