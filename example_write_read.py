"""Three examples of WRITE and READ functions. This code is based on SoloLearn lectures and has educational purposes; no copyright infringement is intended."""

# FIRST EXAMPLE

msg = "Hello world!"
file = open("newfile.txt", "w")
amount_written = file.write(msg)
print(amount_written)
file.close()

file = open("newfile.txt", "r")
amount_written = file.read()
print(f"{amount_written} \n")
file.close()

# SECOND EXAMPLE

file = open("newfile.txt", "w")
file.write("Some text")
file.close()

file = open("newfile.txt", "r")
print("Reading 1st file contents:")
print(f"File content: {file.read()}")
print("End of the 1st part \n")
file.close()

# THIRD EXAMPLE

file = open("newfile.txt", "w")
file.write("Some new text")
file.close()

file = open("newfile.txt", "r")
print("Reading 2nd file contents:")
print(f"File content: {file.read()}")
print("End of the 2nd part")
file.close()
