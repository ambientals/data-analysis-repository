"""Code that creates a list with user-input numbers. This code has educational purposes; no copyright infringement is intended."""

# creating an empty list  
lst = [] 

# inputting the number of elements as input  
n = int(input("Enter number of elements: ")) 

# iterating till the end of the range  
for i in range(0, n): 
    ele = int(input(f"Enter the #{i+1} element: ")) 
    lst.append(ele) 

# adding the element  
print(lst)