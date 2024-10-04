def change(amount_due, amount_paid):

    change = amount_paid - amount_due  # change that needs to be given back
    # bills and coins that are currently available in cents
    denominations =[(20000, 'R200'), (10000, 'R100'), (5000, 'R50'), (2000, 'R20'), (1000, 'R10'), (500, 'R5'), (200, 'R2'), (100, 'R1'), (50, '50c'), (20, '20c'), (10, '10c'), (5, '5c')]

    change_dict = {}  # to store bills or coins we giving back
    for value, name in denominations:  # for every bill/coin we give back
        
        count = change // value  # use floor division so we can get the largest whole number, how much of denomination we can use

        if count > 0:
            change_dict[name] = count  # we add count to dictionary if we give at least one bill/coin, it then becomes rand/cent
            change -= count * value  # subtract the value of the total change

    return change_dict  # return the dictonary that showsthe change to give out.

