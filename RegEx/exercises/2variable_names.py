import re

sentance = input()
# pattern = r'\b_([A-Za-z0-9]+)\b'
pattern = r"\b_([a-zA-Z0-9]+)\b"
matches = re.findall(pattern, sentance)
print(",".join(matches))
