def password_validator(password):
    Upper_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    strength_length = 0  # initializing so that it can add one until it gets to 8
    # Use boolean to store, so that if condition is met it changes and becomes True otherwise it stays False
    char_in_uppercase = False
    char_in_digits = False
    for char in password:
        strength_length +=1  # increase for each character.

        if char in Upper_letters:
            char_in_uppercase = True
        else:
            return "No uppercase letter present"
        if char in digits:
            char_in_digits = True
        else:
            return "No digit present"
    if strength_length >=8:
        return True
    else:
        return "Password length is less than 8."
    if strength_length and char in Upper_letters and char in digits:
        return password

#print(f"Your password is good to go!")
print(password_validator("caDeau@7"))