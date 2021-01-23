N = 4
L = [
    "+++===!!!!","777777......TTTTTTTTTTTT","(AABBC)", "3.1415555"
    ]
    
final_l = []
for line in L:
    current_symbol = line[0]
    current_count = 0
    current_string = ""
    for symbol in line:
        if current_symbol == symbol:
            # same symbol as before
            current_count += 1
        else:
            # add to string with count and symbol
            current_string += str(current_count) + " "
            current_string += current_symbol + " "
            # new symbol, update current symbol, and add to count
            current_symbol = symbol
            current_count = 1
    # for the last symbol once the for loop finishes
    current_string += str(current_count)+ " "
    current_string += symbol
    final_l.append(current_string) # add the compressed data to the list
    
print(final_l)