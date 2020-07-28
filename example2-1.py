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
# print(tup)
import array

# The array constructor takes two arguments, so the parentheses around the
# generator expression are mandatory. The first argument of the array constructor
# defines the storage type used for the numbers in the array,
array = array.array("I", (ord(symbol) for symbol in symbols))
# print(array)


# ------------------------------------------
""" tuple
"""
# example 2-7
# lax_coordinates = (33.9425, -118.408056)
# city, year, pop, chg, area = ("Tokyo", 2003, 32450, 0.66, 8014)
# traveler_ids = [("USA", "221345"), ("BRA", "sdf551423"), ("ESP", "ashf53454")]
# for passport in traveler_ids:
#     print(passport)

# for passport in sorted(traveler_ids):
#     print("%s/ %s" % passport)

# for country, _ in traveler_ids:
#     print(country)


# --------------------------------------------
# example 2-8

# metro_areas = [
#     ("Tokyo", "JP", 36.933, (35.689722, 139.691667)),
#     ("Delhi NCR", "IN", 21.935, (28.613889, 77.208889)),
#     ("Mexico City", "MX", 20.142, (19.433333, -99.133333)),
#     ("New York-Newark", "US", 20.104, (40.808611, -74.020386)),
#     ("Sao Paulo", "BR", 19.649, (-23.547778, -46.635833)),
# ]

# print("{:15} | {:^9} | {:^9}".format("Name", "lat.", "long."))
# fmt = "{:15} | {:9.4f} | {:9.4f}"

# for name, cc, pop, (latitude, longitude) in metro_areas:
#     print(fmt.format(name, latitude, longitude))


# ------------------------------------------------
# example 2-9
# from collections import namedtuple

# city = namedtuple("City", "name country population coordinates")
# toko = city("toko", "iraq", 6.23456, (52.6456, 19.5644))
# print(toko)
# print(toko.country)


# ----------------------------------------------
# example 2-10

# from collections import namedtuple

# city = namedtuple("City", "name country population coordinates")
# toko = city("toko", "iraq", 6.23456, (52.6456, 19.5644))
# print(city._fields)

# baghdad = namedtuple("baghdad", "bag dad")
# baghdad_data = ("baghdad time", "IQ", "millons", baghdad(654, 321))
# baghdad = city._make(baghdad_data)

# print(baghdad._asdict())

# for feild, value in baghdad._asdict().items():
#     print(f"{feild}:", value)

# print(baghdad.__add__(toko))

# ----------------------------------------------------
"""
SLICING
"""
# l = "bicycle  a lot of item to buy"
# print(l[1:20:2])
# print(l[2:])

# print(l[:3])
# print(l[3:])

# ---------------------------------------------------------

# l = list(range(18))
# print(l)

# print(l[2:5])

# del l[5:7]
# print(l)

# l[3::10] = [11, 22]
# print(l)

# l[2:5] = 100
# print(l)

# l[2:5] = [100]
# print(l)

# my_list = [[1, 2, 4]] * 3
# print(my_list)

# ------------------------------
"""
Building lists of lists
"""

# board = [["_"] * 3 for i in range(3)]
# print(board)
# board[0][1] = "X"
# print(board)
# the same of above
# board = [["_"] * 3] * 3
# print(board)
# board[0][1] = "X"
# print(board)

# -----------------------------
"""
Augmented Assignment with Sequences

"""

# example 2-14
# t = (1, 2, [30, 40])
# t[2] += [50, 60]
# print(t)

# sorted makes a new list
# fruits = ["grape", "respberry", "apple", "banana"]
# print(sorted(fruits, key=len, reverse=True))

# list.sort() changes the same objects
# fruits.sort()
# print(fruits)
# --------------------------------------------------
"""
Managing ordered sequences with bisect
"""

# Searching with bisect


# example 2-17
import bisect
import sys

# my_list = [1, 5, 11, 13, 16, 20]
# smaller = [0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 15, 21, 23, 27]

# fow = "{0:2d} @ {1:2d}  {2}{0:<2d}"


# def demo(bisect_fn):
#     for needle in reversed(smaller):
#         position = bisect_fn(my_list, needle)
#         offset = position * "   |"
#         print(fow.format(needle, position, offset))


# if __name__ == "__main__":
#     bisect_fn = bisect.bisect_left
#     print("DEMO:", bisect_fn.__name__)
#     print("my_list ->", "  ".join("%2d" % n for n in my_list))
#     demo(bisect_fn)
# ----------------------------------------------------------------------

# example 2-18


import bisect
import sys


def grade(score, breakpoint=[60, 70, 80, 90], grades="FDCBA"):
    i = bisect.bisect(breakpoint, score)
    return grades[i]


print([grade(score) for score in [33, 99, 77, 70, 12, 100]])
# ---------------------------------------------------------------

# Inserting with bisect.insort
