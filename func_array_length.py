"""Function that calculates an array's length. This code has educational purposes; no copyright infringement is intended."""

def array_length(array):
    length_variable = 0
    for unit in array:
        length_variable +=1
    print(f"The {array} array's length is: " + str(length_variable))
    
array_length("python")