#Write a program to print the following triangle.

n=int(input("enter the n value"))
k=5

print("print the following triangle")
for i in range(0,n):
    for j in range(i+1):

       print(k,end=' ')
    k-=1


    print()