#Write a program to print the following triangle.
#              1
#           1  2
#        1   2  3
#     1    2  3 4
#   1  2  3  4  5

print("print the following triangl")

n = int(input("enter the n value:"))
for i in range(n):
    for j in range(i,n):
        print(' ', end=' ')
    for j in range(i+1):
        print(j+1,end=' ')

    print()