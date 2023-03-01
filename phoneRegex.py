import re

# create a regex obect
phone_num_regex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")

# pass string you want to search into the regex object search() method
mo = phone_num_regex.search("My number is 847-767-0468")

# call group() method to return a string of the actual matched text
print("Phone number found: " + mo.group())

# create groups of the regex with paranthesis
phoneNumRegex = re.compile(r"(\d\d\d)-(\d\d\d-\d\d\d\d)")

mo = phoneNumRegex.search("My number is 415-555-4242.")

# retrieving each object grouping
print(mo.group(1))
print(mo.group(2))

# retrieve a list of all the groupings
print(mo.groups())
