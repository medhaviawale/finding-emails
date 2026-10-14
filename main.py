import re

with open('Student_details.txt', 'rt') as fh:
    data = fh.read()

pattern = r"\b[a-zA-Z][\w.-]+[@][a-z]+[.][a-z]+\b"
match_obj = re.finditer(pattern, data)

for match in match_obj:
    print(match)
