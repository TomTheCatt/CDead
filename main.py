#Clears the terminal screen
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

#Installs a module via the system terminal
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

#Main program
def main():
    cls()
    #opens and seperates dead_words.txt
    with open("dead_words.txt", "r") as file:
        dead_words = file.readline().split("-")
        #Removes spaces and empty indexes from list
        for index in dead_words:
            dead_words.remove(index) if index == "" else None
    #opens and seperates dead_words.txt
    with open("punctuation.txt", "r") as file:
        punctuation = file.readline().split("@@")
        #Removes spaces and empty indexes from list
        for index in punctuation:
            punctuation.remove(index) if index == "" else None
    #Takes in user input from a file called type_in_here.txt
    with open("type_in_here.txt", "r") as file:
        eList = []
        for line in file:
            eList.append(line)
        eList = repr("".join(eList))
        #Cleans up essays
        essay, nEssay = str(eList).replace(r"\n", r" \n "), str(eList).replace(r"\n", r" \n ")#Seperates new line for further refrence
        essay, nEssay = "".join(essay), "".join(nEssay)#Joins together
        essay, nEssay = essay.replace("\\", ""), nEssay.replace("\\", "")#Removes "\"
        essay, nEssay = essay[1:-1], nEssay[1:-1]#Removes the ' at the beginning and end of the essays
    print(f"{Fore.GREEN}Processing your file. . .{Style.RESET_ALL}")
    #Goes through each word and removes the punctuation
    for x in punctuation:
        nEssay = nEssay.replace(str(x), "")
    #print(f"{nEssay}\n{essay}")
    #Goes through each word and detects if they are a dead word
    nEssay, essay, count, in_quotation = nEssay.split(), essay.split(), {}, False
    for i in range(len(nEssay)):
        try:
            word = nEssay[i]
        except:
            continue
        #Detects if the words are in a quotation. If they are, it will skip them entirely and move on until it reaches the end quotation.
        if '"' in word:
            in_quotation = False if in_quotation == True else True
        for dword in dead_words:
            if in_quotation == True:
                break
            #Checks single words
            essay[i] = f"{Back.RED}{essay[i]}{Style.RESET_ALL}" if word.lower() == dword.lower() else essay[i]
            #Checks two words
            try:
                essay[i], essay[i+1] = f"{Back.RED}{essay[i]}" if word.lower() in dword.lower() and nEssay[i+1].lower() in dword.lower() and len(word) > 2 else essay[i], f"{essay[i+1]}{Style.RESET_ALL}" if word.lower() in dword.lower() and nEssay[i+1].lower() in dword.lower() and len(word) > 2 else essay[i+1]
            except:
                pass
            #Adds to the counter if the word was not previously counted. If it was, it will add "1" to that counter.
            count.update({str(dword): 0}) if dword.lower() == word.lower() else None
            try:
                count[str(dword)] = count[str(dword)]+1 if dword.lower() == word.lower() else count[str(dword)]
            except:
                pass
    essay = " ".join(essay)
    #Adds a new line if the raw text "\n" is detected.
    essay = essay.replace(r"\n", "\n")
    print(f"{essay}\n")
    print(f"{Fore.GREEN}No dead words found.{Style.RESET_ALL}") if count == {} else None
    for key in count:
        print(f"{key.capitalize()}: {count[key]}")
        time.sleep(0.1)
    user_input = input("\n(y/n) Redo processing?  ")
    main() if user_input == "y" else None

#Installs needed imports and installations if __name__ is "__main__"
if __name__ == "__main__":
    print("Importing os. . .")
    import os
    print("Importing subprocess. . .")
    import subprocess
    print("Importing sys. . .")
    import sys
    print("Installing colorama. . .")
    install("colorama")
    print("Importing colorama. . .")
    from colorama import Fore, Back, Style, init
    print("Initalizing colorama. . .")
    init()
    print("Importing time. . .")
    import time
    print("Clearing terminal. . .")
    main()
