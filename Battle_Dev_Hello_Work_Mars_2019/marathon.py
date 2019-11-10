import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip("\n"))

place = int(lines[0])

for i in lines[1:]:
    en_plus, en_moins = map(int, i.split(" "))
    place = place - en_moins + en_plus

if place <= 100:
    print(1000)
elif place > 100 and place <= 10000:
    print(100)
else:
    print("KO")
