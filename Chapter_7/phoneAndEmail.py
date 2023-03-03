#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.
import re
import pandas as pd

phoneRegex = re.compile(
    r"""(
(\d{3}|\(\d{3}\))?  # area code
(\s|-|\.)?          # separator
(\d{3})             # first 3 digits
(\s|-|\.)           # separator
(\d{4})             # last 4 digits
(\s*(ext|x|ext.)\s*(\d{2,5}))? # extension
)""",
    re.VERBOSE,
)

mo = phoneRegex.search("My number is 847-767-0468")

print(mo.groups())

# TODO: Create email regex.
# username
# @ sign
# domain name
# dot - something

emailRegex = re.compile(
    r"""(
[a-zA-z0-9._%+-]+    # username
@                    # @ sign
[a-zA-Z0-9.-]+       # domain name
(\.[a-zA-Z]{2,4})     # dot - something
)""",
    re.VERBOSE,
)

mo2 = emailRegex.search("My email is fisherrjd@gmail.com")
print(mo2.groups())

# TODO: Find matches in clipboard text

copied_text = str(testfile)
matches = []
for groups in phoneRegex.findall(copied_text):
    phoneNum = "-".join([groups[1], groups[3], groups[5]])
    if groups[8] != "":
        phoneNum += " x" + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(copied_text):
    matches.append(groups[0])

print(matches)

# TODO: Copy results to the clipboard.
