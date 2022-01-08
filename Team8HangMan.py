# Introduction
print("Welcome! Let's play Hangman :)")

# Ask Player 1 to input the word
# Making it lower case so it's not case sensitive
print("Your word will be transformed to be all lowercase.")
word = input("Player 1 - Enter the word to be guessed: ").lower()

# Check if word input is valid (no numbers, symbols, or blank spaces)
validWord = False
while validWord == False:
  if word.isalpha() and " " not in word:
    validWord = True
  # If the input is invalid, re-enter the input
  else:
    validWord = False
    word = input("Sorry, that's an invalid input. Player 1 - Enter the word to be guessed: ")

# Ask Player 1 to input the number of lives
numGuess = input("Player 1 - Enter the number of lives: ")

# Check if lives input is valid (no letters, symbols, spaces, and a whole number above 0)
validNumGuess = False
while validNumGuess == False:
  if numGuess.isdecimal() and int(numGuess)>0:
    validNumGuess = True
  # If the input is invalid, re-enter the input
  else:
    validNumGuess = False
    numGuess = input("Sorry, that's an invalid input. Player 1 - Enter the number of lives: ")

# Transition to Player 2
print("\n Thanks Player 1!")
print("Let's get started :)")

print("\n"*50)
print("Hello, Player 2!")
print("You have " + numGuess + " guess(es)")

wordGuessed = False

# Ask Player 2 for their guess
# Making it lower case so it's not case sensitive
guess = input("Player 2 - Enter a letter to guess: ").lower()

# Creating the word to display on screen
hiddenWord = []
for letter in word:
  hiddenWord.append("_")

numGuess = int(numGuess)

# If Player 2 still has guesses left and they have not guessed the word, continue the game
while (numGuess >= 1) and (wordGuessed == False):
  # Checking if Player 2's guess is valid (it's made up of letters and is not more than one letter)
  if not guess.isalpha() or len(guess) != 1:
    print("Invalid input.")
  # If Player 2's guess is in the word, print "Correct" and decrease number of guesses
  elif guess in word:
    print("Correct.")
    numGuess -= 1
    # Adjusting the displayed word so that Player 2's guess shows
    i = 0
    for letter in word:
      if guess == letter:
        hiddenWord[i] = guess
      i += 1
    # If Player 2's guess is not in the word, print "Incorrect" and decrease number of guesses
  else:
    print("Incorrect.")
    numGuess -= 1

  # Checking if Player 2 has guessed the word completely
  # If so, exit out of the loop and declare Player 2 the winner
  hiddenWordStr = ""
  for letter in hiddenWord:
    hiddenWordStr += letter
  if hiddenWordStr == word:
    wordGuessed = True
    break

  # Display information
  print("WORD: " + hiddenWordStr)
  print("GUESSES LEFT: "+str(numGuess))

  # Ask Player 2 for input again
  # Check to ensure that the number of guesses are still above 0 after they have been subtracted
  if numGuess>0:
    guess = input("Player 2 - Enter a letter to guess: ").lower()

# If Player 2 has guessed the word, Player 2 wins
if wordGuessed == True:
  print("Congratulations, Player 2 wins! You have guessed the word!")
# If Player 2 did not guess the word, Player 1 wins
else:
  print("Player 2 did not guess the word. Congratulations, Player 1 wins!")
  print("The word was " + word)
