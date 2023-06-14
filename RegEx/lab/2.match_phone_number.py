import re

words = input()
pattern = r"\+359-2-\d{3}-\d{4}\b|\+359 2 \d{3} \d{4}\b"
matches = re.findall(pattern, words)
print(", ".join(matches))