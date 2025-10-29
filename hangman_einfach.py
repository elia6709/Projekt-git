import random
import sys
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




words_tiere = ["APFEL", "HAUS", "BAUM", "TISCH", "STUHL", "FENSTER", "TÜR", "LAMPE", "SOFA", "TEPPICH", "SCHRANK", "REGAL", "BUCH", "HEFT", "STIFT", "PAPIER", "UHR", "HANDY", "COMPUTER", "MAUS", "TASTATUR", "BILDSCHIRM", "FERNSEHER", "RADIO", "KAMERA", "FOTO", "BILD", "SPIEGEL", "VASE", "BLUME", "PFLANZE", "TOPF", "HERD", "OFEN", "KÜHLSCHRANK", "MIKROWELLE", "WASSERKOCHER", "TASSE", "GLAS", "TELLER", "MESSER", "GABEL", "LÖFFEL", "SCHÜSSEL", "TOPFDECKEL", "SEIFE", "ZAHNBÜRSTE", "ZAHNPASTA", "HANDTUCH", "SHAMPOO", "DUSCHGEL", "KAMM", "BÜRSTE", "FÖHN", "RASIERER", "CREME", "MANTEL", "JACKE", "HOSE", "HEMD", "T-SHIRT", "PULLOVER", "KLEID", "ROCK", "SCHUHE", "SOCKEN", "MÜTZE", "SCHAL", "HANDSCHUHE", "BRILLE", "RUCKSACK", "TASCHE", "GELDBEUTEL", "SCHLÜSSEL", "AUTO", "FAHRRAD", "ROLLER", "BUS", "ZUG", "BAHN", "FLUGZEUG", "SCHIFF", "BOOT", "STRASSE", "WEG", "BRÜCKE", "TUNNEL", "AMPEL", "SCHILD", "KREUZUNG", "PARKPLATZ", "GARAGE", "TANKSTELLE", "SCHULE", "UNIVERSITÄT", "LEHRER", "SCHÜLER", "KLASSE", "TAFEL", "KREIDE", "LINEAL", "ZIRKEL", "ATLAS", "GLOBUS", "SPORT", "BALL", "TOR", "NETZ", "SCHLÄGER", "TRIKOT", "RENNEN", "SCHWIMMEN", "SPRINGEN", "TURNEN", "MUSIK", "LIED", "TON", "KLANG", "RHYTHMUS", "MELODIE", "GITARRE", "KLAVIER", "GEIGE", "TROMMEL", "FLÖTE", "SAXOPHON", "MIKROFON", "KONZERT", "BÜHNE", "THEATER", "FILM", "KINO", "SCHAUSPIELER", "REGISSEUR", "SZENE", "DREHBUCH", "LICHT", "PUBLIKUM", "APPLAUS", "ZEITUNG", "ARTIKEL", "BERICHT", "SCHLAGZEILE", "REDAKTION", "JOURNALIST", "INTERVIEW", "MEINUNG", "KOMMENTAR", "POLITIK", "REGIERUNG", "MINISTER", "PRÄSIDENT", "PARTEI", "WAHL", "GESETZ", "POLIZEI", "FEUERWEHR", "ARZT", "KRANKENHAUS", "PATIENT", "MEDIKAMENT", "REZEPT", "SPRITZE", "VERBAND", "OPERATION", "THERAPIE", "GESUNDHEIT", "KRANKHEIT", "FIEBER", "HUSTEN", "SCHMERZ", "BLUT", "HERZ", "LUNGE", "MAGEN", "KOPF", "BEIN", "ARM", "HAND", "FUSS", "FINGER", "ZEH", "HAUT", "AUGE", "OHR", "NASE", "MUND", "ZAHN", "STIMME", "SPRACHE", "WORT", "SATZ", "TEXT", "BUCHSTABE", "GRAMMATIK", "BEDEUTUNG", "FRAGE", "ANTWORT"]

words_informatik

words_Länder

words_körperteile

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
██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗
██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║
███████║███████║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║
██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║
██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝

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
            print("""                                                    
   __      __   __  __  __    ___     ___     ___      __    ___    
 /'_ `\  /'__`\/\ \/\ \/\ \  / __`\ /' _ `\ /' _ `\  /'__`\/' _ `\  
/\ \L\ \/\  __/\ \ \_/ \_/ \/\ \L\ \/\ \/\ \/\ \/\ \/\  __//\ \/\ \ 
\ \____ \ \____\\ \___x___/'\ \____/\ \_\ \_\ \_\ \_\ \____\ \_\ \_\
 \/___L\ \/____/ \/__//__/   \/___/  \/_/\/_/\/_/\/_/\/____/\/_/\/_/
   /\____/                                                          
   \_/__/                                                           
""")
            print('Yep! Das gesuchte Wort ist "' + secretWord + '"! Du hast gewonnen!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        if len(missedLetters) == len(HANGMANPICS) - 1:
            displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
            print('''
 __  __                 ___                                  
/\ \/\ \               /\_ \                                 
\ \ \ \ \     __   _ __\//\ \     ___   _ __    __    ___    
 \ \ \ \ \  /'__`\/\`'__\\ \ \   / __`\/\`'__\/'__`\/' _ `\  
  \ \ \_/ \/\  __/\ \ \/  \_\ \_/\ \L\ \ \ \//\  __//\ \/\ \ 
   \ `\___/\ \____\\ \_\  /\____\ \____/\ \_\\ \____\ \_\ \_\
    `\/__/  \/____/ \/_/  \/____/\/___/  \/_/ \/____/\/_/\/_/                                                   
''')
            print('Du hast alle Versuche verbraucht\nNach ' + str(len(missedLetters)) + ' falschen Versuchen und ' + str(len(correctLetters)) + ' korrekten Versuchen, wäre das Wort "' + secretWord + '" gewesen')
            gameIsDone = True

    while gameIsDone:
        missedLetters = ''
        correctLetters = ''
        secretWord = getRandomWord(words)
        jaodernein = str(input('Willst du nochmals Spielen? Ja = 1, Nein = 2 '))

        if jaodernein == '1':
            print('Viel Glück')
            gameIsDone = False

        elif jaodernein == '2':
            print('Danke fürs Spielen')
            sys.exit()
            


        #Falls der Spieler nochmals spielen will, muessen alle Variablen (missedLetters, correctLetters) wieder geleert werden und gameIsDone auf False gesetz werden
        #Auch sollte ein neues Wort in secretWord ueber die Methode getRandomWord(words) gewaehlt werden
