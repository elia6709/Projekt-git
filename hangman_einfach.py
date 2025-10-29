import random
HANGMANPICS = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']




#Erstelle eine Liste aus Worten in der Form ['informatik', 'hardware', 'switch'] usw.
#Da diese Eingabe als Liste sehr muehsam ist, kannst du auch einen String eingeben un diesen splitten. "wort wort".split()

words = ['NETZKARTE', 'ETHERNET', 'ALGORITHMUS', 'BETRIEBSSYSTEM', 'NETZWERK', 'DATENBANK', 'SPEICHER', 'LAPTOP', 'LINUX']



#Waehle ein zufaelliges Wort aus der Liste wordList und gib dieses mit return zurück
def getRandomWord(words):
    wort = random.choice(words)
    return wort

def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
    print(HANGMANPICS[len(missedLetters)])
    print()

    print('Falsche Buchstaben:', end=' ')
    #Zeige hier alle falschen Buchstaben hintereinander an, welche in missedLetters gespeichert sind.
    #hier kommt dein Code
    print(missedLetters)


    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)): 
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks: 
        print(letter, end=' ')
    print()


#Hier soll ein Buchstabe vom Benutzer abgefragt werden. Aber Achtung nur ein Buchstabe.
#Falls es eine Zahl, mehrere Buchstaben oder ein Sonderzeichen oder nichts ist. Wiederhole die Abfrage
def getGuess(alreadyGuessed):
    while True:
        derBuchstabe = input('Gib einen einzelnen Buchstaben ein: ').upper()

        if derBuchstabe in alreadyGuessed:
            print('Dieser Buchstaben wurde bereits eingegeben')

        elif len(derBuchstabe) == 1 and derBuchstabe.isalpha():
            break
        
        else:
            print('Gib nur einen Buchstaben ein!')
        #if derBuchstabe == correctLetters
    return derBuchstabe

#Willst Du nochmals spielen? Frage den Spieler. Als Rueckgabewert wird True oder False erwartet.
def playAgain():
    #hier kommt dein Code
    return #hier kommt dein Code


#Hier beginnt das Programm
#Gib einen schoenen Titel aus, damit der Benutzer weiss, worum es geht
print("""
H   H   A   N   N  GGGG  M   M   A   N   N
H   H  A A  NN  N G      MM MM  A A  NN  N
HHHHH AAAAA N N N G  GG  M M M AAAAA N N N
H   H A   A N  NN G   G  M   M A   A N  NN
H   H A   A N   N  GGGG  M   M A   A N   N

""")
#hier kommt dein Code

missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)

    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yep! Das gesuchte Wort ist "' + secretWord + '"! Du hast gewonnen!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        if len(missedLetters) == len(HANGMANPICS) - 1:
            displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
            print('Du hast alle Versuche verbraucht\nNach ' + str(len(missedLetters)) + ' falschen Versuchen und ' + str(len(correctLetters)) + ' korrekten Versuchen, wäre das Wort "' + secretWord + '" gewesen')
            gameIsDone = True

    if gameIsDone:
        missedLetters = ''
        correctLetters = ''
        secretWord = getRandomWord(words)
        jaodernein = str(input('Willst du nochmals Spielen? Ja = 1, Nein = 2 '))

        if jaodernein == '1':
            print('Viel Glück')
            gameIsDone = False

        elif jaodernein == '2':
            print('Danke fürs Spielen')
            break

        else:
            print('1 oder 2!')


        #Falls der Spieler nochmals spielen will, muessen alle Variablen (missedLetters, correctLetters) wieder geleert werden und gameIsDone auf False gesetz werden
        #Auch sollte ein neues Wort in secretWord ueber die Methode getRandomWord(words) gewaehlt werden
