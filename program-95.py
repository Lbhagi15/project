#Write a program to print the following triangle.

#1 2 3 4 5
# 1 2 3 4
#   1 2 3
#     1 2
n=5
for i in range(n):
    for j in range(i):
        print(" ", end=' ')
    for j in range(n-i):
         print(j+1, end=' ')
    print()