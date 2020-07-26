"""
list comprehensions or listcomps

"""
symbols = "@#(&*$%"
codes = []
for symbol in symbols:
    codes.append(ord(symbol))
# print(codes)

# ----------------------------------
symbols = "@#(&*$%"
codes = [ord(symbol) for symbol in symbols]
# print(codes)
# ----------------------------------
# in py3 listcomps and genexps and their siblings have their
#  own local scope

x = "ABC"
dummy = [ord(x) for x in x]
# print(x)
# print(dummy)
# ----------------------------------
# liscomps do everything the map and filter functions do
symbols = "(*^&%"
beyond_ascii = [ord(s) for s in symbols if ord(s) < 127]
# print(beyond_ascii)

symbols = "(*^&%"
beyond_ascii = list(filter(lambda c: c < 127, map(ord, symbols)))
# print(beyond_ascii)

colors = ["black", "white"]
sizes = ["S", "M", "L"]
tshirts = [(color, size) for color in colors for size in sizes]
# print(tshirts)
# --------------------------------------
# --------------------------------------

""""
Generator Expressions or genexp

"""
# show the basic usage of genexps to build a tuple and an array.

# If the generator expression is the single argument in a function call, there is no
# need to duplicate the enclosing parentheses.

symbol = "(*^&*%^"
tup = tuple(ord(symbol) for symbol in symbols)
print(tup)
import array

# The array constructor takes two arguments, so the parentheses around the
# generator expression are mandatory. The first argument of the array constructor
# defines the storage type used for the numbers in the array,
array = array.array("I", (ord(symbol) for symbol in symbols))
print(array)
