import random
user_input = int(input("Please choose fom the three: 0 = scissor, 1 = rock, 2 = paper "))
computer_input = random.randint(0, 2)

# conditions
if computer_input == user_input:
    print("Its a draw, play again.")
elif user_input > 2:
    print("You entered an invalid number, you lost.")
elif user_input < computer_input:
    print("You lost!")
elif user_input == 0 and computer_input == 2:
    print("You lost.")
elif user_input == 2 and computer_input == 0:
    print("You lost!")
elif computer_input < user_input:
    print("You win!")

#print(user_input)
print(computer_input)
