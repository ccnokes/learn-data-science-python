# comments
# hello world
print("Hello world!")

# at the repl, help() is useful for seeing the documentation for a function or data structure

# variables
# variables are dynamically typed and mutable. No consts.
a = 1
print(a)
a = "hello"

# tuples and ranges
t = (1, 2)
r = range(1, 10, 2)  # (1, 3, 5, 7, 9)
# tuple-ify a range
tuple(r)

# lists
l = [1, 2, 3, 4]
# concat lists with "+" operator
concatted = [1, 2] + [3, 4]  # [1, 2, 3, 4]
# in-place, mutative concat with .extend()
l.extend([5, 6])  # l = [1, 2, 3, 4, 5, 6]
# lists have methods like append, index, insert, pop, remove, reverse, sort
l.index(2)  # = 1 (like findIndex in JS)
l[-2]  # 3, can use negative indices to access from the end

# slices
l[:2]  # [1, 2]  (like slice in JS)
l[1:3]  # [2, 3]

# dictionaries / hashmaps
map = {"a": 1, "b": 2}
# note dictionaries in Python are guaranteed to be insertion ordered
map.keys()  # ['a', 'b']

# equality comparisons
[1, 2] == [1, 2]  # True
{"a": 1, "b": 2} == {"a": 1, "b": 2}  # True

# "in" keyword
1 in (1, 2, 3)  # True
10 not in range(1, 11)  # False
1 in [1, 2]  # True
"a" in {"a": 1, "b": 2}  # True
1 in {"a": 1, "b": 2}  # False

# loops
for i in range(10):
    print(i)

# to iterate over a sequence and also have access to the index, use enumerate
for i, v in enumerate(range(5, 20, 2)):
    print(i, v)

# list comprehension
# create a list by iterating over a sequence
# this is a common idiom
[x for x in range(10)]  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[x * 2 for x in [0, 1, 1, 2, 3, 5, 8]]  # [0, 2, 2, 4, 6, 10, 16]

# functions


def add(x, y):
    return x + y


add(1, 2)  # 3


# can strongly type arguments and return values
# doesn't do anything at runtime
# VSCode has a setting to show type hints
def sum(x: int, y: int) -> int:
    return x + y


def reverse(str):
    return str[::-1]


def reverse2(str):
    ret = ""
    for i in range(str):
        ret += str[i]
    return ret


# try/catch and exceptions
def throw_error():
    try:
        raise Exception("error")
    except Exception as e:
        print("caught error", e)


# classes
class Counter:
    ohyeah = True  # class static variable

    def __init__(self, init_count=0):  # constructor
        self.count = init_count  # instance variable. Note no "private" keyword

    def increment(self):  # methods are passed reference to self as first arg
        self.count += 1

    def decrement(self):
        self.count -= 1


c = Counter(5)  # no new keyword
c.increment()
c.decrement()
print("c count =", c.count)  # 5


# class inheritance
# multiple inheritance is allowed
class CounterChild(Counter):
    def increment_by_2(self):
        self.count += 2


c2 = CounterChild(4)
c2.increment_by_2()
print("c2 count =", c2.count)  # 6
