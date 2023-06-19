def validateInput(n):
    if n is None:
        print("Cannot enter nothing. Please try again.")
        return False
    
    # checks if input is only numeric using method. Negative values contain '-' and floats contain '.' so it is not only numeric.
    if not n.isnumeric():
        print("Cannot enter non integer or negative integer. Please try again.")
        return False
    n = int(n)
    if n % 2==0:
        print("Cannot enter even value. Please try again.")
        return False
    return True

# Validates where the pointer should point and returns the point
def validPointer(i,j,arr):
    row = i-1 # checks 1 row above
    col = j+1 # one column to the right
    
    # if the pointer moves out of the grid for the top point pointer at the bottom/end
    if row<0:
        row=len(arr)-1
    
    # if the pointer moves out of the grid from the right point pointer on the left of grid
    if col==len(arr):
        col=0
    
    # if a pointer space is filled then move the pointer one row down only
    if arr[row][col] == 0:
        return (row,col)
    else:
        row = i+1
        col =j
        if row>len(arr):
            row=0
        return (row,col)
    
# returns a grid of n*n and fills it with valid values
def generateMagicSquare(n):
    arr = [[0 for _ in range(n)] for _ in range(n)] # square of n*n size
    i = 0
    j = (n//2 ) # middle value of n
    count = 0
    while count!=(n*n): # number of values/count goes from 1 up to n^2 as a rule of magic squar of specific order n
        count+=1
        arr[i][j] = count
        i,j = validPointer(i,j,arr)
    return arr

# checks all the rows, columns and diagonals match magic constant returns true if all pass else false if any one fails
def validateMagicSquare(arr,n):
    M = n*((n**2+1)/2)
    c3=0
    c4 = 0
    
    for i in range(n):
        c1 =0
        c2=0
        for j in range(n):
            c1 += arr[i][j] # sum of the row (n times check)
            c2 += arr[j][i] # sum of a column (n times check)
        if c2!=M or c1!=M:
            return False
        c3 += arr[i][i] # sum of diagonal(top-left to bottom-right)
        c4 += arr[n-i-1][n-i-1] # sum of diagonal(bottom-left to top-right)
    if c3!=M or c4!=M:
        return False
    else:
        return True



def main():
    N = input("Enter odd positive integer: ")
    while not validateInput(N):
        N = input("Enter odd positive integer: ")

    # we know it is an into so can make it an int without an error
    N = int(N)
    arr = generateMagicSquare(N)
    for row in range(N):
        for col in range(N-1):
            print(f"{arr[row][col]:5d}",end="")
        print(f"{arr[row][-1]:5d}")
    if validateMagicSquare(arr,N):
        print("correct")

main()
# time complexity = O(2n^2) validatin grid + filling grid
# space complecity = O(n^2) grid space

    
        