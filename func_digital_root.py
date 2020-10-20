"""This function takes an N number and sums all its digits until it gets reduced to only one digit. 
Examples: 
16  -->  1 + 6 = 7
132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
This code is based on CodeWars katas and has educational purposes; no copyright infringement is intended."""

def digital_root(n):
    sum = 0
    for items in str(n):
        sum += int(items)
    newsum = 0
    while len(str(sum)) > 1:
        for items in str(sum):
            newsum += int(items)
        sum = newsum
    return sum

print(digital_root(16))
print(digital_root(132189))