def compare_codes(guess, secret_code):

    correctcolor_pos = 0  # it will increase by 1 for every color that is correct and in right position
    correctish_color = 0  # will increase by one just foer correct color

    unmatched_secret = []  #anything that does not match for position put into list so we can loop through again and see matches
    unmatched_guess = []
    
    # calculate the right positions using indexing for accurate position
    # since there are 4 colours the range should be 4 
    for i in range(4):
        if guess[i] == secret_code[i]:  # loops through the colors positions
            correctcolor_pos += 1
        else:
            unmatched_secret.append(secret_code[i])  # these dont match position so we gonna loop through for color
            unmatched_guess.append(guess[i])

    for color in unmatched_guess:
        if color in unmatched_secret:
            correctish_color += 1  # for every color in secret code we increment

    return(correctcolor_pos, correctish_color)
