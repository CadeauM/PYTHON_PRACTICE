def is_password_secure(password):
    if len(password) < 8:
        return False
    special_charactrs = "!@#$%&*()<>?-~+"
    uppercase_letters = False
    lowercase_letters = False
    digits = False
    special = False
    
    for char in password:  # so it loopsthrough each character
        if char.isupper():  # we are gonna start if statements and not use elif because all conditions need to be met
            uppercase_letters = True
        if char.islower():
            lowercase_letters = True
        if char.isdigit():  # returns true if theres at least one digit
            digits = True
        if char in special_charactrs:
            special = True
        if uppercase_letters and lowercase_letters and digits and special:
            return True  # return True if all conditions are met.
    
    return False  # if conditions arent met even if it is one it should return False

#is_password_secure("Pass123@me")

