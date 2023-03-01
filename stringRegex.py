import re

# The pipe will match on either of the 2 options
heroRegex = re.compile(r"Batman|Tina Fey")

# Batman occurs first
mo1 = heroRegex.search("Batman and Tina Fey.")
print(mo1.group())

# Tina Fey occurs first
mo2 = heroRegex.search("Tina Fey and Batman.")
print(mo2.group())

print()
batRegex = re.compile(r"Bat(man|mobile|copter|bat)")
mo = batRegex.search("Batmobile lost a wheel")
print(mo.group())
print(mo.group(1))
