###
# author : Andres Mrad (Q-ro)
# Description : A clompletely pointless guessing game
###
import random

def PickNumber(rangeStart, rangeEnd):
	return random.randint(rangeStart,rangeEnd)

def ValidateDifficulty ():
	validDifficulty = False
	print('''Select difficulty :\n
1) Noob.\n
2) Human.\n
3) Hacker.\n
4) Impossible.\n ''')
	while not validDifficulty:
		try:
			selection  = int(input('Enter difficulty: '))
		except ValueError:
			print('That\'s not even a number')
			continue
		else:
			if selection >= 1 and selection <=4:
				validDifficulty = True
				return selection
			else:
				print('That is not a valid option')

def PrintGreet():
	print('''Hello, welcome to number guesser,
it\'s good that you want to waste time.\n''')

def GuessNumber(number):
	gameNotOver = False
	while not gameNotOver:
		try:
			guess = int(input('Tell me your guess'))
		except ValueError:
			print('That\'s not even a number')
			continue
		else:
			if guess == number:
				print('You did it !')
				gameNotOver = True
			elif guess > number:
				print('The number is smaller')
			elif guess < number:
				print('The number is bigger')

guessing = True
guessedCorrectly = False
chosenOne = False
numberToGuess = 0

PrintGreet()
difficulty = ValidateDifficulty()

if difficulty == 1:
	numberToGuess = PickNumber(0,3)
elif difficulty == 2:
	numberToGuess = PickNumber(0,10)
elif difficulty == 3:
	numberToGuess = PickRange(0,100)
elif difficulty == 4:
	numberToGuess = PickRange(0,100000000)
else:
	print('''I don\'t know how you did it, but this is not a valid 
option, to the corn field with you !''')

GuessNumber(numberToGuess)
