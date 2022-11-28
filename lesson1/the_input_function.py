# Request a user input with the `input` function!
# We can also add text for this request inside our function.

filename = input("Filename: ")
extension = input("Extension: ")
print(filename, extension, sep=".")  # First solution
print(filename, ".", extension, sep="")  # An equivalent, second solution
