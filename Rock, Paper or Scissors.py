import random	
computer_move = random.randint(0,2)

if computer_move == 0:
	computer_move = "rock"
elif computer_move == 1:
	computer_move = "paper"
elif computer_move == 2:
	computer_move = 'scissors'

print("Rock, Paper or Scissors?: ")
# .lower() turns all input to lower case to make it easy to make the game 
player_move = input ("").lower()
print(computer_move)

if computer_move == player_move:
	print("Tie!")

elif player_move == "rock":
	if computer_move == "scissors":
		print("You Win!")
	elif computer_move == "paper":
		print("You Lose!")

elif player_move == "paper":
	if computer_move == "rock":
		print("You Win!")
	elif computer_move == "scissors":
		print("You Lose!")

elif player_move == "scissors":
	if computer_move == "paper":
		print("You Win!")
	elif computer_move == "rock":
		print("You Lose!")

else:
	print("Enter a valid value!")
