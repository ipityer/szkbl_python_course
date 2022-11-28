print("Szuzuki ")  # Print the word Szuzuki, and then a new line!

print(5 * "Szuzuki ")  # We can multiply strings with integers to repeat them.

var1 = "Hello"
var2 = "világ!"

# We can separate the arguments inside `print` with a comma.
# The printed variable values will be separated by a space by default.
# There can be any number of (positional) arguments inside `print`.
print(var1, var2)

# We can separate the strings by a different value through the `sep` positional argument.
print(var1, var2, sep="/")

# We can also switch out the newline character inside `print`.
print(var1, var2, end=" ENTER ")
print("This will appear in the same line!")

# To put all of these together:
print(var1, " SOMETHING ", var2, sep="_", end=" THE END!")
