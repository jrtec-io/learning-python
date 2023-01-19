def concatenate(first_word, *args):
    attachment = ""
    for word in args:
        attachment += "-" + word
    return (first_word + attachment )


print(concatenate("I", "love", "Python", "!"))


"""
Adding Words

You need to write a function that takes multiple words as its argument and returns a concatenated version of those words separated by dashes (-).
The function should be able to take a varying number of words as the argument.

Sample Input
this
is
great

Sample Output
this-is-great
Recall, using *args as a function parameter enables you to pass an arbitrary number of arguments to that function.
"""