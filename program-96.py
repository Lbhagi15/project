#Write a program to print the following triangle.
#1 2 3 4 5
#  2 3 4 5
#    3 4 5
#      4 5
#        5

print("print the following triangle")


n=int(input("enter the n value:"))
for i in range(n):
    for j in range(i):
        print(" ", end=' ')
    for j in range(n-i-1,-1,-1):
         print(n-j,end=' ')
    print()