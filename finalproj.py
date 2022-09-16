
#Instructions for Our Game:
#Open final.py
#Make sure that the text document "words.txt" is in the same directory as "final.py". 
#In terminal, create a board by typing w=Wordle(5,6)
#Next, type w.hostGame() and select among the given options
#Type in 5 letter words and try to guess the right word!
#When the game is over, if you wish to play again, repeat the instructions, starting at 3)
#If you want to quit the game, just type quit in the terminal when you are asked to input a random word.

#Thanks for playing!


import random
def get_text(filename): #used to get access to dictionary of 5 letter words
        f = open(filename, encoding = 'latin1')
        text = f.read()
        f.close()
        return text

def mmenu():
    """Prints the menu of options that the user can choose."""
    print()
    print("(1) Human V Human")
    print("(2) Human V AI")
    print("(3) AI V AI")


class Wordle:
    "A data type that represents the game Wordle"
    
    def __init__(self, width, height):
        """Construct objects of type Wordle, with the given width and height."""
        self.width = width
        self.height = height
        self.data = [[' ']*width for row in range(height)]
        self.wrongLetters = []
        self.correctLetters = []
        self.rightSpot = []

        # We do not need to return anything from a constructor!

    def __repr__(self):
        """This method returns a string representation
           for an object of type Board.
        """
        s = ''                          # The string to return
        for row in range(0, self.height):
            s += '|'
            for col in range(0, self.width):
                s += self.data[row][col] + '|'
            s += '\n'

        s += (2*self.width + 1) * '-'   # Bottom of the board
        s += '\n'
        for i in range(0, self.width):
            s += ' ' + str(i) # Add code here to put the numbers underneath

        return s       # The board is complete; return it

    
    
    def addMove(self,col,ox):
        """
        This method takes two arguments: the first, col, represents the index 
        of the column to which the letter will be added. The second argument, 
        ox, will be a 1-character string representing the letter to add to the board. 
        That is, ox should either be an alphabet
        """
        H = self.height
        for row in range(0,H):
            if self.data[row][col] != ' ':
                self.data[row-1][col] = ox
                return
        self.data[H-1][col] = ox

    def isFull(self):
        """
        return True if the calling object (of type Board) is completely full of checkers. 
        It should return False otherwise
        """
        H = self.height
        W = self.width
        D = self.data
        for row in range(H):
            for col in range(W):
                if D[row][col] == ' ':
                    return False
        return True

    def choose_word(self):
        """
        Computer chooses random 5 letter word from dictionary
        """
        w = self.width 
        h = self.height 
        
        word = get_text("words.txt")
        words = []
        words = word.split("\n")
        x = random.choice(words)
        x = x.lower()
        return x

    def match(self,wordx,guess): 
        """
        If user guesses right position for letter, letter is upper-cased
        if user guesses only right letter not right position, a lower case version of
        letter appears on board
        If user guesses wrong letter, letter + X appears on board
        """
        newString = ''
        visible = ''
        for x in range(0,5):
            if guess[x:x+1] == wordx[x:x+1]:
                if guess[x:x+1] not in self.rightSpot:
                    self.rightSpot += guess[x:x+1]
                newString = guess[x:x+1].upper()
                self.addMove(x,newString)
                visible += newString
            elif guess[x:x+1] in wordx:
                if guess[x:x+1] not in self.correctLetters:
                    self.correctLetters += guess[x:x+1]
                newString = guess[x:x+1].lower()
                self.addMove(x,newString)
                visible += newString
            else:
                if guess[x:x+1] not in self.wrongLetters:
                    self.wrongLetters += guess[x:x+1]
                newString = '?'
                self.addMove(x,newString)
                visible += newString
        
        print("Incorrect letters:")
        print(self.wrongLetters)
        
        print("Correct letters:")
        print(self.correctLetters)
        print("Correct letters in the right spot:")
        print(self.rightSpot)
        #print(visible)
    
    def identify_guess(self,wordx,guess): 
        """
        If user guesses right position for letter, letter is upper-cased
        if user guesses only right letter not right position, a lower case version of
        letter appears on board
        If user guesses wrong letter, letter + X appears on board
        """
        newString = ''
        visible = ''
        for x in range(0,5):
            if guess[x:x+1] == wordx[x:x+1]:
                newString = guess[x:x+1].upper()
                #self.addMove(x,newString)
                visible += newString
            elif guess[x:x+1] in wordx:
                newString = guess[x:x+1].lower()
                #self.addMove(x,newString)
                visible += newString
            else:
                newString = '?'
                #self.addMove(x,newString)
                visible += newString
        return visible
    
    def aiMove(self, visible):
        """ Looks at user input. If any Capital letters in user input, creates a list from 
        word list of words having that capital letter in correct position. If any lower case letters
        in Guess, creates a shorter list with Capital letter and small letter.If no correct letters in Guess, randomly selects word
        from text file 
        """

        Lol = []                           # Empty list
        word = get_text("words.txt")     
        words = []
        words = word.split("\n")      #separate list with all the words from the dictionary
             

        
        for l in range(5):
            for word in words:
                if ord(visible[l]) >= ord('A') and ord(visible[l]) <= ord('Z'):
                    #print(l)
                    #print(len(visible))
                    #print(len(word))
                    #print(word)
                    if visible[l].lower() == word[l]:
                        Lol += [word]
                elif ord(visible[l]) >= ord('a') and ord(visible[l]) <= ord('z'):
                    Lol += []
                else:
                    Lol += []
        
        if Lol == []:
            Lol = words
        
        Lol2 = []  # creates new list : Lol2
        
        for l in range(len(visible)):
            for word in Lol:
                if ord(visible[l]) >= ord('a') and ord(visible[l]) <= ord('z'):
                    if visible[l] in word:
                        Lol2 += [word]
                else:
                    Lol2 += []
        
        if Lol2 == []:
            Lol2 = Lol
        
        #print(Lol)
        #print(Lol2)
        comp = random.choice(Lol2)
        print("Computer guessed: ",comp )
        return comp

    
    #this function randomly chooses a word for words.txt
    def hostGame(self):
        """
        Play the game of Wordle. If menu is 1, human plays human. If menu is 2, human plays against AI
        If menu is 3, AI plays against AI
        """

        while True:       # The user-interaction loop

            mmenu()
        
            menu = input("Choose an option: ")

            

            #
            # "Clean and check" the user's input
            # 
            try:
                menu = int(menu)   # Make into an int!
            except:
                print("I didn't understand your input! Continuing...")
                continue


            if menu == 1:

                wordx = self.choose_word() #takes word from previous function
            
                word = wordx.lower() #puts word in lowercase

                #print(word)

                print(self)

                for live in range(6): #this gives us 5 lives
                    guess = input("Choose a word:  ") #user guess
                
                    if guess == 'quit':
                        print('Better luck next time!')
                        return
                
                    while guess not in (get_text("words.txt")).lower():
                        guess = input("Choose another word:  ") 

                    self.match(word,guess)       
                    print(self)

                    if guess == word:
                        print('You win!')
                        return

                print("You Lose!! The word was:" + word) #use if last guess is wrong
                return  

            if menu == 2:
                wordx = self.choose_word() #takes word from previous function
                #print(wordx)
            
                word = wordx.lower() #puts word in lowercase

                print(self)
            
                for live in range(6): #this gives us 5 lives
                    guess = input("Choose a word:  ") #user guess

                    if guess == 'quit':
                        print('Better luck next time!')
                        return

                    while guess not in (get_text("words.txt")).lower():
                        guess = input("Choose another word:  ") 
                
                    self.match(word,guess)       
                    print(self)
                
                    if guess == word:
                        print('You win!')
                        return
                        
                    visible = self.identify_guess(wordx,guess)

                    comp = self.aiMove(visible)
                    self.match(word,comp)       
                    print(self)


                    if comp == word:
                        print('AI wins!')
                        return

                    if self.isFull():
                        break  


                print("You both Lose!! The word was:" + word) #use if last guess is wrong
                return

            if menu == 3:

                wordx = self.choose_word() #takes word from previous function
                #print(wordx)
            
                word = wordx.lower() #puts word in lowercase

        
                print(self)

                comp2 = '?????'

                for live in range(5): #this gives us 5 lives

                    visible = self.identify_guess(wordx, comp2)

                    comp1 = self.aiMove(visible)
                    self.match(word,comp1)       
                    print(self)


                    if comp1 == word:
                        print('AI 1 wins!')
                        return

                    visible = self.identify_guess(wordx, comp1)

                    comp2 = self.aiMove(visible)
                    self.match(word,comp2)       
                    print(self)


                    if comp2 == word:
                        print('AI 2 wins!')
                        return

                    if self.isFull():
                        break  


                print("You both Lose!! The word was:" + word) #use if last guess is wrong
                return