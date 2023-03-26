from math import ceil

def printMove(indexOfZero, indexOfOne, numCols):
    
    x1 =  (indexOfOne + 1) % numCols
    if x1 == 0: ## Since we are using mod, column will be 0 if we are at a multiple of numCols but me want it to be numCols instead
        x1 = numCols

    y1 = ceil((indexOfOne+1)/numCols)
    
    x2 = (indexOfZero+1) % numCols
    if x2 == 0:
        x2 = numCols
    
    y2 = ceil((indexOfZero+1)/numCols)

    print(f"Move the egg in column {x1} of row {y1} to column {x2} of row {y2}")


def minSwapBalance(bStr):
    n = len(bStr)
    numRows = int(input("How many rows?: "))
    numCols = int(input("How many cols?: "))

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
    print(mismatches)
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
test = [0,0,0,1,0,1,1,1,0,1,1,0,1,1,0,1,0,1]
minSwapBalance(test)
