# This Write a program to print the following triangle.
#Write a program to print the following triangle.
#1 1 1 1 1
#2 2 2 2
#3 3 3
#4 4
#5

n=int(input("enter the n value:"))

print("print the following triangle")
for i in range(n):
    for j in range(n - i):
        print(i + 1, end=' ')



    print()


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
