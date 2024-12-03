# Use nested loops to print a pyramid pattern of *.
num=int(input("Please Enter Number of Star rows"))
for row in range(num):
    for col_space in range(num-row-1):
        print(" ",end='')
    for stars in range(2*row+1):
        print("*",end='')
    print()