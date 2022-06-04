#Write a program to print the following triangle.
#1 1 1 1 1
#2 2 2 2
#3 3 3
#4 4
#5

print("print the following triangle")
n=6

for i in range(1,n):

    for j in range(i,n):

        print(i, end=' ')
    print()
