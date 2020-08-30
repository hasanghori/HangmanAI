def solve(letter, lettersArray, numberOfLetters):
    numberOfTimes = int(input("how many times does the specified letter appear in your word"))
    for x in range(0, numberOfLetters):
            print(lettersArray[x], end=" ")
    print()
    indexList = []
    for x in range(1, numberOfTimes+1):
        index = int(input("What is the spot number " + str(x) + " that this letter occurs"))
        indexList.append(index)
        lettersArray[index-1] = letter
    return indexList

def remove(lettersArray, words, shortList, indexList):
    shortList.clear()
    stringWorksList = []
    for x in range(0, len(words)):
        string = words[x]
        count = 0
        for y in range(0, len(indexList)):
            if string[int(indexList[y])-1] == lettersArray[int(indexList[y])-1]:
                count += 1
        stringWorksList.append(count)
    for x in range(0 , len(words)):
        string = words[x]
        if stringWorksList[x] == len(indexList):           
            shortList.append(string)
    words.clear()
    for x in range(0, len(shortList)):
        words.append(shortList[x])
    
    print("I have this many options left " + str(len(words)))

def noResponseRemove(words, letter, shortList):
    shortList.clear()
    for x in range(0, len(words)):
        str = words[x]
        if str.find(letter) == -1:
            shortList.append(str)
    words.clear()
    for x in range(0, len(shortList)):
        words.append(shortList[x])
    
    print("I have this many options left", end = " ")
    print(len(words))
    
def removeLength(numberOfLetters, words, shortList):
    for x in range(0, len(words)-1):
        if len(words[x]) == numberOfLetters:
            shortList.append(words[x])
    
    words.clear()
    for x in range(0, len(shortList)):
        words.append(shortList[x])
    shortList.clear()
    print("I have this many options left " + str(len(words)))
    
def chooseNextLetter(words, alphabet, counter, chosenLetters):
    counter = [int(0),int(0),int(0),int(0),int(0),int(0),int(0),int(0),int(0),int(0),int(0),int(0),int(0),int(0),int(0),int(0),int(0),int(0),int(0),int(0),int(0),int(0),int(0),int(0),int(0),int(0)] 
    for x in range(0, len(words)):
        string = words[x]
        for y in range(0, len(alphabet)):
            for z in range(0, len(string)):
                if string[z] == alphabet[y]:
                    counter[y]+=1
                    break
    index = int(0)
    value = len(words)
    notAlreadyChosenList = [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]
    notAlreadyChosen = True
    for x in range(0, len(counter)):
        notAlreadyChosen = True
        for y in range(0, len(chosenLetters)):
            if x == chosenLetters[y]:
                notAlreadyChosen = False
        notAlreadyChosenList[x] = notAlreadyChosen
    print(notAlreadyChosenList)
    print(counter)
    print(alphabet)        
    for x in range(0, len(counter)):
        if (len(words) - counter[x]) < value:
            if(notAlreadyChosenList[x] == True):
                value =  int(abs((len(words)) - counter[x]))
                index = int(x)
            
    chosenLetters.append(index)
    return(alphabet[index]) 

def SelectWord(words):
    if len(words) == 1:
        return True
    else:
        return False 

def printPic(wrongGuess):
    HANGMAN = (
        """
        -----
        |   |
        |
        |
        |
        |
        |
        |
        |
        --------
        """,
        """
        -----
        |   |
        |   0
        |
        |
        |
        |
        |
        |
        --------
        """,
        """
        -----
        |   |
        |   0
        |  -+-
        |
        |
        |
        |
        |
        --------
        """,
        """
        -----
        |   |
        |   0
        | /-+-
        |
        |
        |
        |
        |
        --------
        """,
        """
        -----
        |   |
        |   0
        | /-+-\ 
        |
        |
        |
        |
        |
        --------
        """,
        """
        -----
        |   |
        |   0
        | /-+-\ 
        |   | 
        |
        |
        |
        |
        --------
        """,
        """
        -----
        |   |
        |   0
        | /-+-\ 
        |   | 
        |   | 
        |
        |
        |
        --------
        """,
        """
        -----
        |   |
        |   0
        | /-+-\ 
        |   | 
        |   |
        |  /
        |
        |
        --------
        """,
        """
        -----
        |   |
        |   0
        | /-+-\ 
        |   | 
        |   | 
        |  / \ 
        |   
        |
        --------
        """)
    print(HANGMAN[wrongGuess])
    
#Main Method
print("Let's play hangman")

chosenWord = input("Type in anything when you have chosen your word. Personally I find it convenient to type my word here but that is your choice")
print("Respond yes or no to the following questions")
chosenLetters = [4]#equivalent to e which is the most common letter in the alphabet
words = []
shortList = []
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
counter = [int(0),int(0),int(0),int(0),int(0),int(0),int(0),int(0),int(0),int(0),int(0),int(0),int(0),int(0),int(0),int(0),int(0),int(0),int(0),int(0),int(0),int(0),int(0),int(0),int(0),int(0)]
print(len(counter))
print(len(alphabet))
f = open("USenglish.txt", "r")
fline = f.readlines()
for x in fline: #
    words.append(x) #builds a list of 70,000 words
for x in range(0, len(words)):
    words[x] = words[x].replace("\n", "")

numberOfLetters = int(input("how many letters is your word"))
removeLength(numberOfLetters, words, shortList)
print(len(words))
lettersArray = []

for x in range(0, numberOfLetters):
    lettersArray.append("_")
    print(lettersArray[x], end=" ")
print()#just a quick enter

wrongGuess= int(0)
letter = 'e'
indexList=[]
while wrongGuess <= 7:
    response = input("does the letter " + letter + " appear in your word")
    if response == "yes":
        indexList = solve(letter, lettersArray, numberOfLetters)
        remove(lettersArray, words, shortList, indexList)
        guessWord = SelectWord(words)
        if guessWord:
            print("I figured out your word")
            print(words[0])
            break
        
        for x in range(0, numberOfLetters):
            print(lettersArray[x], end=" ")
    elif response == "no":
        print("my bad")
        noResponseRemove(words, letter, shortList)
        wrongGuess+=1
        print("I now have "+ str(wrongGuess) + " wrong guesses out of a max of 8")
        for x in range(0, numberOfLetters):
            print(lettersArray[x], end=" ")
    printPic(wrongGuess)
    letter = chooseNextLetter(words, alphabet, counter, chosenLetters)
    printWord = input("would you like to print out all the options")
    if printWord == "yes":
        print(words)
if wrongGuess <= 7:
    print("yeah that was too easy, you think you could choose a harder word next time XD")
else:
    print("Wow so you won. Let's play again and this time plz don't misspell your word -_-")
    
