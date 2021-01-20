import re

phone_number = "+358 50-123-456789"

print(re.match(r"^\+?\d{1,20}$", re.sub(r"[ -]", "", phone_number)))

result = str(re.match(r"^\+?\d{1,20}$", re.sub(r"[ -]", "", phone_number))) # Mysteeririvit
result = re.search('\+\d+', result)                                         # Mysteeririvit
print(result.group(0))                                                      # Mysteeririvit
