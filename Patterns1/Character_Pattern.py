'''Print the following pattern for the given N number of rows.
Pattern for N = 4
A
BC
CDE
DEFG'''


## Read input as specified in the question
## Print the required output in given format
n = int(input())
i = 1
while i<=n:
    j = 1
    while j<=i:
        startchr = chr(ord('A')+ i - 1)
        chrint = chr(ord(startchr)+ j - 1)
        print(chrint, end='')
        j = j+1
    print()
    i = i+1