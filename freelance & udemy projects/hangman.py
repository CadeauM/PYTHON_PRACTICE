import random

list_of_words = ['baboon', 'clouds', 'lion']

chosen_word = random.choice(list_of_words)
print(chosen_word)

word_length = len(chosen_word)
blanks = ""
for i in range(word_length):
    blanks += "_ "  # we use strings because we are adding strings to a string.
print(blanks)  # print should be out of loop so that it can print the final product

correct_word = []  # create empty list so we can append and retrieve and not loose words
lives = 6
game = True

while game:
    display = ""  # we create a new variable because if we dont then we printing the blanks twice creating confusion.
    guess = input("Guess a letter: ").lower()
    
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_word.append(letter)  # we append every correct guess into the list.
        elif letter in correct_word:
            display += letter
        else:
            display += "_ "  # Do not use the is and elif/ else statements it confuses a lot of thing, create a complete different statement.
    
    print(display)

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game = False
            print("You lose...")
    
    if "_" not in display:
        game = False
        print("You win!")
