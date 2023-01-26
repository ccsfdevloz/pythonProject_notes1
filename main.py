# First edit of program
#
# Example 1
#

print()
print('Example 1:')
first = 4
second = first
print('first: {}'.format(first))
print('second: {}'.format(second))
# Do first and second point to the same place in memory,
# or are they two distinct things that happen to be the same?

first = first + 3
print('first: {}'.format(first))
print('second: {}'.format(second))
# What do you think now?
# Do first and second point to the same place in memory,
# or are they two distinct things that happen to be the same?

#
# Example 2
#

print()
print('Example 2:')
first = 'Erez'
second = first
print('first: {}'.format(first))
print('second: {}'.format(second))
# Do first and second point to the same place in memory,
# or are they two distinct things that happen to be the same?

first = first + ' Powell'
print('first: {}'.format(first))
print('second: {}'.format(second))
# What do you think now?
# Do first and second point to the same place in memory,
# or are they two distinct things that happen to be the same?

#
# Example 3
#

print()
print('Example 3:')
first = [ 'Erez', 'is', 'a' ]
second = first
print('first: {}'.format(first))
print('second: {}'.format(second))
# Do first and second point to the same place in memory,
# or are they two distinct things that happen to be the same?

first.append('teacher.')
print('first: {}'.format(first))
print('second: {}'.format(second))
# What do you think now?
# Do first and second point to the same place in memory,
# or are they two distinct things that happen to be the same?

#
# Example 4
#

print()
print('Example 4:')
first = 'Hello.'
second = first
print('first: {}'.format(first))
print('second: {}'.format(second))
# Do first and second point to the same place in memory,
# or are they two distinct things that happen to be the same?

# Try this line of code by removing the # and running the code:
# first[5] = '!'
# It will fail. Why?
# What does "TypeError: 'str' object does not support item assignment" mean?
# When you are done, add the # back in front of the bad code.
first = first.replace('.', '!')
print('first: {}'.format(first))
print('second: {}'.format(second))
# What do you think now?
# Do first and second point to the same place in memory,
# or are they two distinct things that happen to be the same?

#
# Example 5
#

print()
print('Example 5:')
first = [ 'Erez', 'is', 'a', 'teacher.' ]
second = first
print('first: {}'.format(first))
print('second: {}'.format(second))
# Do first and second point to the same place in memory,
# or are they two distinct things that happen to be the same?

first[3] = 'instructor.'
second[3] = 'engineer.'
print('first: {}'.format(first))
print('second: {}'.format(second))
# What do you think now?
# Do first and second point to the same place in memory,
# or are they two distinct things that happen to be the same?
# -------------------------------------------------

# Observations
# int, float, and str are value types - this means that the value is copied from one variable to another every time you use the assignment operator
# even if two value variables currently have the same value, changing one of them does not affect the other
# lists (and other objects) are reference types - this means that when you use the assignment operator you are actually telling the variable on the left to point to the same place in memory as the variable on the right
# if two reference variables currently point to the same place in memory, changing the contents of one of them will change the contents of the other (because they're the same thing)
# One Step Further
# This is even more important with functions. When you call a function

# Any argument that is a value variable will have its value copied into the corresponding parameter.
# Any argument that is a reference variable will have the reference copied into the corresponding parameter.
# Example Code - With Functions
# -------------------------------------------------

#
# Example 1
#

def addOne(x):
    x = x + 1
    print('x is {}'.format(x))

print()
print('Example 1:')
someVariable = 4
print('someVariable: {}'.format(someVariable))

# Will this change the contents of someVariable?
addOne(someVariable)
# What does that tell you about how this argument is sent?
# Is that 'call by value' or 'call by reference'?

#
# Example 2
#

def setToOne(x):
    x[0] = 1
    print('x is {}'.format(x))

print()
print('Example 2:')
someVariable = [ 3, 7, -19, 2, 5, 7 ]
print('someVariable: {}'.format(someVariable))

# Will this change the contents of someVariable?
setToOne(someVariable)
# What does that tell you about how this argument is sent?
# Is that 'call by value' or 'call by reference'?