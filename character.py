import re
"""pattern=r"[aeiou]"
if re.match(pattern,"anuuinnud"):
    print("match")"""
"""pattern = r"[A-Z]"
if re.match(pattern, "Aanuuinnud"):
    print("match")"""
"""pattern = r"[0-9]"
if re.match(pattern, "0Aanuuinnud"):
    print("match")"""
pattern = r"[0-9][A-Z][a-z]"
if re.match(pattern, "0Aanuuinnudz"):
    print("match")
