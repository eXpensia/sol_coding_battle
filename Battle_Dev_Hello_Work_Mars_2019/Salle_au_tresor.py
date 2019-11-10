import sys

N = int(input())

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))


result = ""

for y in range(N):
    for x in range(N):
        if lines[y][x] == "o":
            result += "x"
        if x < (N-1):
            result += ">"
    result += (N-1)*"<"
    if y < (N-1):
        result += "v"

result += (N-1)*"^"

for y in range(N):
    for x in range(N):
        if lines[y][x] == "*":
            result += "x"
        if x < (N-1):
            result += ">"
    if y < (N-1):
        result += "v"
        result += (N-1)*"<"


print(result)
