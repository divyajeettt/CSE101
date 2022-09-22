FILENAME: str = ".\\Data\\Q1\\question1_input.txt"


def readfile() -> str:
    """returns the entire file contents as a string"""
    
    with open(FILENAME) as file:
        contents = file.read()
    return contents
    

def frequency(word: str) -> int:
    """returns the count of the word in the file"""
    
    # instead of writing the code for opening and reading again, 
    # it is more efficient to use the code written above
    return readfile().split().count(word)


def unique_words() -> list[str]:
    """returns a list contating unique words from the file"""
    
    # dictionary keys are always unique
    return list(word_counts().keys())


def word_counts() -> dict[str, int]:
    """returns a dictionary mapping each word to its frequency 
    in the file"""
    
    contents = readfile().split()
    return {word: contents.count(word) for word in contents}


def replace(word1: str, word2: str) -> int:
    """replaces all occurences of word1 with word2 in the File
    returns the number of replacements made
    returns 0 if word1 does not exist in the file"""
    
    if frequency(word1) == 1:
        return 0

    with open(FILENAME) as file:
        contents = file.readlines()
    
    n = 0
    for i, line in enumerate(contents):
        line = line.split()
        for j, word in enumerate(line):
            if word == word1:
                line[j] = word2
                n += 1
        contents[i] = " ".join(line)

    with open(FILENAME, "w") as file:
        file.write("\n".join(contents))
        
    return n


def main() -> None:
    """__main__ function"""
    
    while True:
        print("Enter 1. to display the frequency of a specifc word")
        print("Enter 2. to display all unique words")
        print("Enter 3. to display the counts of all words")
        print("Enter 4. to replace a word with another word")
        print("Enter 5. to Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "5":
            break
        
        if choice not in tuple("1234"):
            print("INVALID CHOICE: Please enter a number from 1-5 \n")
            continue
        
        if choice == "1":
            word = input("Enter the word to count: ")
            if (count := frequency(word)) == 0:
                print("Word does not exist in the file")
            else:
                print(f"{word !r} occurs {count} time(s) in the file")
        
        elif choice == "2":
            print(*unique_words(), sep=" ; ")
        
        elif choice == "3":
            for word, count in word_counts().items():
                print(f"{word}: {count}")
        
        else:
            word1 = input("Enter word you wish to replace: ")
            word2 = input("Enter replacement: ")
            if not (n := replace(word1, word2)):
                print(f"{word1 !r} does not exist in the file")
            else:
                print(f"{word1 !r} replaced with {word2 !r} successfully")
                print(n, "replacement(s) made")
                
        print()


if __name__ == "__main__":
    main()