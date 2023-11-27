from math import ceil

# Converts a string index to row and column
# positions in a carton with numCols columns.
def string_index_to_row_col(index, numCols):
    column = (index % numCols) + 1
    row = ceil((index + 1)/numCols)

    return (row, column)

# Prints a move
# Ex: Move the egg in column 3 of row 4 to column 5 of row 3
def print_move(emptyIndex, eggIndex, numCols):
    emptyRow, emptyColumn  = string_index_to_row_col(emptyIndex, numCols)
    eggRow, eggColumn = string_index_to_row_col(eggIndex, numCols)

    print(f"Move the egg in column {eggColumn} of row {eggRow} to column {emptyColumn} of row {emptyRow}")

# Main function
# Assumes that bStr is of even length
def min_swap_balance(bStr, numCols):
    n = len(bStr)

    # Find mismatched pairs
    mismatches = [[], []]
    for i in range(n//2):
        if bStr[i] != bStr[n-i-1]:
            if bStr[n-i-1] == 0:
                mismatches[0].append(n-i-1)
            else:
                mismatches[1].append(n-i-1)

    ## The string is already a palindrome
    if mismatches[0] == mismatches[1]:
        return bStr

    # Swap mismatched pairs
    for i in range(min(len(mismatches[0]), len(mismatches[1]))):
        zero = mismatches[0].pop(0)
        one = mismatches[1].pop(0)
        bStr[zero] = 1
        bStr[one] = 0
        print_move(zero, one, numCols)

    # Since mismatched pairs have all been resolved, the only
    # remaining mismatches can be due to an unequal amount of 1's in each
    # half. Thus, we must simpy swap the remaining unbalanced 1's
    if mismatches[0]:
        temp = bStr[n-mismatches[0][1] - 1]
        bStr[n-mismatches[0][1]- 1] = bStr[mismatches[0][0]]
        bStr[mismatches[0][0]] = temp
        print_move(n-mismatches[0][1]-1, mismatches[0][0], numCols)
    else:
        temp = bStr[n-mismatches[1][1] - 1]
        bStr[n-mismatches[1][1] - 1] = bStr[mismatches[1][0]]
        bStr[mismatches[1][0]] = temp
        print_move(n-mismatches[1][1]-1, mismatches[1][0], numCols)
        
    return bStr

if __name__ == '__main__':
    givenStr = str(input("Enter a string: "))
    bStr = [int(c) for c in givenStr]
    numCols = int(input("How many columns are there?: "))
    min_swap_balance(bStr, numCols)
