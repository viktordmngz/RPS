import random, re

name = input("Please enter your name: ")

#make sure the name only contains letters
while re.search(r"[0-9]", name):
	name = input("Please enter a valid name: ")

#initialize the record variables
wins = 0
losses = 0

#can comment this out if you don't care about ties
#if you don't track ties, be sure to comment out in code below
ties = 0

total = [wins, losses, ties]

#human choice for the game
def human():
	""""
	Want to take an input and make sure it is either rock, paper, or scissors.
	Would also like to take the first letter as an option and accept it.

	If the input is invalid, would like the function to repeat until a valid
	input is put in (kind of like the name above)


	>>> human()

	Please select
	Rock(R), Paper(P), or Scissors(S): Rock
	(valid)

	>>> human()

	Please select
	Rock(R), Paper(P), or Scissors(S): R (or r)
	(valid)

	>>> human()

	Please select
	Rock(R), Paper(P), or Scissors(S): Cats
	(invalid, repeat)

	>>> human()

	Please select
	Rock(R), Paper(P), or Scissors(S): POPPER
	(valid, paper is chosen)
	"""

	choice = input("\nPlease select\nRock(R), Paper(P), or Scissors(S):  ")
	letters = ['r','p','s']

	while choice[0].lower() not in letters:
		choice = input("\nPlease make a valid choice\nRock(R), Paper(P), or Scissors(S):  ")
	
	return choice[0].lower()


def computer():
	"""
	Same as the human function, but for the computer.
	Will need to use a random function and determine a range for the choices.

	0 --> Rock
	1 --> Paper
	2 --> Scissors

	Computer choice is hidden but returned to compare with human()

	>>> computer()
	None
	"""

	# since random will return a number from 0 to just less than 1, multiplying
	# by 3 will return a number from 0 to just less than 3.
	# we can just get the leading int by passing through int()
	choice = int(random.random()*3)

	if choice == 0:
		return 'r'
	elif choice == 1:
		return 'p'
	else:
		return 's'


def game(total, name):
	"""
	total is a list with wins, losses, and ties respectively.
	Ties may be commented out above but the code below must also be adjusted.

	We want to write a way to check quickly if the user chose r, p, or s
	and then we compare it to whether the computer chose r, p, or s.

	*** Note: I don't want to write a bunch of if or elif statements
	*** Maybe alphabetical? p --> r --> s
	*** s --> p would be the only one we would have to check with an if statement
	"""
	a = human()
	b = computer()
	print("Computer chose {}\n".format(b))
	#if a = b, we have a tie and need to exit
	if a == b:
		total[2] += 1
		print("*"*12)
		print("\nYou TIED...this is awkward...\n")
		print("{}'s record: {} wins, {} losses, {} ties\n".format(name, str(total[0]), str(total[1]), str(total[2])))
		print("*"*12)
		return total
	elif a == 'r':
	#Check winning condition if A is rock
		if b == 's':
			total[0] += 1
			print("*"*12)
			print("\nCongrats, {}! You WON!\n".format(name))
			print("{}'s record: {} wins, {} losses, {} ties\n".format(name, str(total[0]), str(total[1]), str(total[2])))
			print("*"*12)
			return total
		else:
			total[1] += 1
			print("*"*12)
			print("\nSorry, {}, you LOST....\n".format(name))
			print("{}'s record: {} wins, {} losses, {} ties\n".format(name, str(total[0]), str(total[1]), str(total[2])))
			print("*"*12)
			return total
	elif a == 'p':
	#Check winning condition if A is paper
		if b == 'r':
			total[0] += 1
			print("*"*12)
			print("\nCongrats, {}! You WON!\n".format(name))
			print("{}'s record: {} wins, {} losses, {} ties\n".format(name, str(total[0]), str(total[1]), str(total[2])))
			print("*"*12)
			return total
		else:
			total[1] += 1
			print("*"*12)
			print("\nSorry, {}, you LOST....\n".format(name))
			print("{}'s record: {} wins, {} losses, {} ties\n".format(name, str(total[0]), str(total[1]), str(total[2])))
			print("*"*12)
			return total
	elif a == 's':
	#Check winning condition if A is scissors
		if b == 'p':
			total[0] += 1
			print("*"*12)
			print("\nCongrats, {}! You WON!\n".format(name))
			print("{}'s record: {} wins, {} losses, {} ties\n".format(name, str(total[0]), str(total[1]), str(total[2])))
			print("*"*12)
			return total
		else:
			total[1] += 1
			print("*"*12)
			print("\nSorry, {}, you LOST....\n".format(name))
			print("{}'s record: {} wins, {} losses, {} ties\n".format(name, str(total[0]), str(total[1]), str(total[2])))
			print("*"*12)
			return total

#to play, call game(total, name)
