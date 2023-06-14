import re
single_string = input()

pattern = r'\b[A-Z][a-z]+\s[A-Z][a-z]+\b'
matches = re.findall(pattern, single_string)
print(" ".join(matches))