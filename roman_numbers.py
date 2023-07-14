# Read the Roman numeral
number = input("Enter a Roman numeral: ")
# We define the variable that will contain the sum of the arabic number
sum = 0
# We define the dictionary of Roman symbols and their values
values = { "M" : 1000, "D" : 500, "C" : 100, "L" : 50, "X" : 10, "V" : 5, "I" : 1}

# Validate if the first symbol is subtracted from the next or just add the value to the total.
def validate_roman_numeral(symbol, next_symbol, symbols, sum, number):
    if next_symbol in symbols:
        sum += values[next_symbol] - values[symbol]
        number = number[1:]
    else:
        sum += values[symbol]
    return sum, number


while len(number) > 0:
    # We obtain the first symbol of the Roman number
    symbol = number[0]
    # We remove the first symbol from the Roman number
    number = number[1:]
    # We check if this is the last symbol
    if len(number) > 0:
        # We get the following Roman number symbol
        next_symbol = number[0]
        # We check if the first symbol is equal to the symbol "I"
        if symbol == "I":
            sum, number = validate_roman_numeral(symbol, next_symbol, ["V", "X"], sum, number)
        if symbol == "X":
            sum, number = validate_roman_numeral(symbol, next_symbol, ["L", "C"], sum, number)
        if symbol == "C":
            sum, number = validate_roman_numeral(symbol, next_symbol, ["D", "M"], sum, number)
        # Only add the value to the total if the first symbol is "V", "L", "D" or "M
        if symbol in ["V", "L", "D","M"]:
            sum += values[symbol]
    # As the last symbol, we add it to the total
    else:
        sum += values[symbol]
# Print the result
print(sum)