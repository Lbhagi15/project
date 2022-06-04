#Write a program to print the following triangle.
#5 5 5 5 5
#4 4 4 4
#3 3 3
#2 2
#1

print("print the follwing triangle")

n = int(input("enter the n value"))      # givening input value by user

for i in range (n):
    for j in range(n-i):
        print(n-i, end=' ')

    print()