def to_roman_numeral(integer):  # input being an integer..

    roman_numeral = ""  # empty string so that it is appended every single time theres a deduction so its saved

    # list of tuples so its sorted from max to the smallest and so its easier loop through and minuses from largest
    symbols_values = [("M",1000), ("CM", 900), ("D", 500), ("CD", 400), ("C", 100), ("L", 50), ("XL", 40), ("X", 10), ("IX", 9), ("V", 5), ("IV", 4), ("I", 1)]
    
    for symbol, value in symbols_values:  # for every tuple in the list
        while integer >= value:  # must be greater than or equal to
            integer -= value
            roman_numeral += symbol  # every symbol is appended to empty string

    return roman_numeral
