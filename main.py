import itertools

## Generates all bit strings of length n
def genBitString(n):
    result = ["".join(seq) for seq in itertools.product("01", repeat=n)]
    return result


## Generates all bit strings up to length n
def genAllBitStrings(n):
    bStrings = {}
    for i in range(1, n+1):
        bStrings[i] = (genBitString(i))

    return bStrings

if __name__ == "__main__":
    n = int(input("Enter a positive integer: "))
    while (n<=0):
        n = int(input("Enter a positive integer: "))
    result = genAllBitStrings(n)
    print(result)
    for i in range(1, n+1):
        print(f"Length {i}: ")
        for num in result[i]:
            print(num)
        print()