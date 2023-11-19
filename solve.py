from math import ceil

def string_index_to_row_col(index, numCols):
    column = (index % numCols) + 1
    row = ceil((index + 1)/numCols)

    return (row, column)

def printMove(emptyIndex, eggIndex, numCols):
    emptyRow, emptyColumn  = string_index_to_row_col(emptyIndex, numCols)
    eggRow, eggColumn = string_index_to_row_col(eggIndex, numCols)

    print(f"Move the egg in column {eggColumn} of row {eggRow} to column {emptyColumn} of row {emptyRow}")

def minSwapBalance(bStr):
    n = len(bStr)
    numCols = int(input("How many columns are there?: "))

    # Find mismatched pairs
    mismatches = [[], []]
    for i in range(n//2):
        if bStr[i] != bStr[n-i-1]:
            if bStr[n-i-1] == 0:
                mismatches[0].append(n-i-1)
            else:
                mismatches[1].append(n-i-1)

    # Swap mismatches pairs
    for i in range(min(len(mismatches[0]), len(mismatches[1]))):
        zero = mismatches[0].pop(0)
        one = mismatches[1].pop(0)
        bStr[zero] = 1
        bStr[one] = 0
        printMove(zero, one, numCols)

    ## The string is already a palindrome
    if mismatches[0] == mismatches[1]:
        return bStr

    # Since mismatched pairs have all been resolved, the only
    # remaining mismatches can be due to an unequal amount of 1's in each
    # half. Thus, we must simpy swap the remainng unbalanced 1's
    # print(mismatches)
    if mismatches[0]:
        temp = bStr[n-mismatches[0][1] - 1]
        bStr[n-mismatches[0][1]- 1] = bStr[mismatches[0][0]]
        bStr[mismatches[0][0]] = temp
        printMove(n-mismatches[0][1]-1, mismatches[0][0], numCols)
    else:
        temp = bStr[n-mismatches[1][1] - 1]
        bStr[n-mismatches[1][1] - 1] = bStr[mismatches[1][0]]
        bStr[mismatches[1][0]] = temp
        printMove(n-mismatches[1][1]-1, mismatches[1][0], numCols)
        
    return bStr

# givenStr = str(input("Enter a string: "))
# bStr = [int(c) for c in givenStr]
bStr= [0,0,0,
       1,0,1,
       1,1,0,
       1,1,0,
       1,1,0,
       1,0,1]
minSwapBalance(bStr)
