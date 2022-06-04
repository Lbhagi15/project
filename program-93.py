# write the program for following  triangle
#5
#5 4
#5 4 3
#5 4 3 2
#5 4 3 2 1

print("print the following triangle")
n=5

for i in  range(0,n ):

    for j in range(i+1):
        print(n-j ,end=' ')
    print()