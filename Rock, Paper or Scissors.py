import random

player_wins = 0
computer_wins = 0

while True:
	num_of_games = input("Best of? ")
	# Keeps asking for input until user enters a number
	try:
		num_of_games = int(num_of_games)
		break
	except:
		print("Invalid Value. Try again. ")

print( f"First to {num_of_games} Wins!\n")

while True:	
	if player_wins == num_of_games:
		print("\nYou have won the game!")
		break
	elif computer_wins == num_of_games:
		print("\nComputer has won the game!")
		break

	print(f'\nPlayers Score: {player_wins}\nComputer Score: {computer_wins}')

	computer_move = random.randint(0,2)

	if computer_move == 0:
		computer_move = "rock"
	elif computer_move == 1:
		computer_move = "paper"
	elif computer_move == 2:
		computer_move = 'scissors'

	# .lower() turns all input to lower case to make it easy to make the game 
	player_move = input ("\nrock, paper or scissors? ").lower()
	if player_move == "quit" or player_move == 'q':
		print("You have succesfully quit the game. ")
		break

	print(f'{computer_move}')


	if computer_move == player_move:
		print("Tie!")

	elif player_move == "rock":
		if computer_move == "scissors":
			print("You Win!")
			player_wins += 1
		elif computer_move == "paper":
			print("You Lose!")
			computer_wins += 1

	elif player_move == "paper":
		if computer_move == "rock":
			print("You Win!")
			player_wins += 1
		elif computer_move == "scissors":
			print("You Lose!")
			computer_wins += 1

	elif player_move == "scissors":
		if computer_move == "paper":
			print("You Win!")
			player_wins += 1
		elif computer_move == "rock":
			print("You Lose!")
			computer_wins += 1

	else:
		print("Enter a valid value!")

print(f'\nPlayers Score: {player_wins}\nComputer Score: {computer_wins}')
print("Thanks for playing!\n")