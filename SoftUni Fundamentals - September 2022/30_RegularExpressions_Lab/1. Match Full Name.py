import re

data = input()
name_verifier = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
verify = re.findall(name_verifier, data)
print(" ".join(verify))