import re

calls = input()
calls_from_sofia = r"\+359-2-\d{3}-\d{4}\b|\+359 2 \d{3} \d{4}\b"
verify = re.findall(calls_from_sofia, calls)
print(", ".join(verify))