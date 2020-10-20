VOWEL_COST = 250
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWELS = 'AEIOU'
SORTED_FREQUENCIES = 'ZQXJKVBPYGFWMUCLDRHSNIOATE'
# Write the WOFPlayer class definition (part A) here

class WOFPlayer:
    
    def __init__(self, name):
        self.name = name
        self.prizeMoney = 0
        self.prizes = []

    def addMoney(self, amt):
        self.prizeMoney = self.prizeMoney + amt
        #return self.prizeMoney
    
    def goBankrupt(self):
        if self.prizeMoney > 0 :
            self.prizeMoney = 0 
            return (self.prizeMoney)
    
    def addPrize(self, prize): 
        self.prizes.append(prize)
    
    def __str__(self):
        return "{} (${})".format(self.name, self.prizeMoney)
    
# Write the WOFHumanPlayer class definition (part B) here

class WOFHumanPlayer(WOFPlayer):

    def getMove(self, category, obscuredPhrase, guessed):
        prompt = "{} has ${}\n\nCategory: {}\nPhrase:  {}\nGuessed: {}\n\nGuess a letter, phrase, or type 'exit' or 'pass':".format(self.name, self.prizeMoney, category, obscured_phrase, guessed)
        userguess = input(prompt)
        return userguess
    
# Write the WOFComputerPlayer class definition (part C) here

class WOFComputerPlayer(WOFPlayer):
    
    SORTED_FREQUENCIES = 'ZQXJKVBPYGFWMUCLDRHSNIOATE'

    def __init__(self, name, diff):
        self.name = name
        self.difficulty = diff
        self.prizeMoney = 0
        self.prizes = []
        
    def smartCoinFlip(self):
        luck = random.randint(1, 10)
        if luck > self.difficulty: 
            return True
        else: 
            return False 
    
    def getPossibleLetters(self, guessed): 
        couldbe = []
        for ch in LETTERS:
            if ch not in guessed:
                couldbe.append(ch)
        if self.prizeMoney < VOWEL_COST:
            for v in VOWELS:
                try: 
                    couldbe.remove(v)
                except Exception: 
                    a = 5
        return couldbe 
    
    def getMove(self, category, obscuredPhrase, guessed):
        if self.getPossibleLetters(guessed) == []:
            return ('pass')
        else: 
            flip = self.smartCoinFlip()
            if flip == True: 
                return (sorted(self.getPossibleLetters(guessed), key = lambda x: SORTED_FREQUENCIES.find(x), reverse=True)[0])
            if flip == False:
                return random.choice(self.getPossibleLetters(guessed))
        
        
        