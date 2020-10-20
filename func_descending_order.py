"""Function that organizes a sequence of numbers into descending order. This code has educational purposes; no copyright infringement is intended."""

def descending_order():
    lst = []
    n = int(input("Enter number of elements: "))
    for i in range(n):
        elemt = int(input("Enter the %d element: " %i))
        lst.append(elemt)

    for i in range (n - 1):
        for j in range(n - i - 1):
            if(lst[j] > lst[j + 1]):
                temp = lst[j]
                lst[j] = lst[j + 1]
                lst[j + 1] = temp

    ret =  lst[::-1]
    return ret

print(descending_order())