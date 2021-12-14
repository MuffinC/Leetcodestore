# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
s= 'VI'
index = 0
counter = 0
add = 0
splitted = [char for char in s]
splitted.append('P')
total = len(splitted)
while (index < total-1):

    if (splitted[index] == 'I'):
        add = 1
        if (splitted[index + 1] == 'V' or splitted[index + 1] == 'X'):
            add = -1
    elif (splitted[index] == 'V'):
        add = 5
    elif (splitted[index] == 'X'):
        add = 10
        if (splitted[index + 1] == 'L' or splitted[index + 1] == 'C'):
            add = -10
    elif (splitted[index] == 'L'):
        add = 50
    elif (splitted[index] == 'C'):
        add = 100

        if (splitted[index + 1] == 'D' or splitted[index + 1] == 'M'):
            add = -100
    elif (splitted[index] == 'D'):
        add = 500
    elif (splitted[index] == 'M'):
        add = 1000
    counter = counter + add
    index += 1
print(counter)