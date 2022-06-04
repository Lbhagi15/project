#Write a program to print the following triangle
#5 4 3 2 1
#5 4 3 2
#5 4 3
#5 4
#5

print("print the following triangle")

n = int(input("enter the  n value"))

for i in range(n):
    for j in range(n - i):
        print(n - j, end=' ')

    print()

