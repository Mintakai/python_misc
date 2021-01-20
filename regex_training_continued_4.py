import re

s = "heights: 170 cm, 60 cm and 175 cm. Weights: 100 kg and 50 kg and a number 3"

print(re.findall(r"(\d+) cm", s))