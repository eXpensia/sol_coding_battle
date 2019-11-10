import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip("\n"))

n_carton = int(lines[0])

masse_tot = 0
n_aller_retour = 0

for i in range(n_carton):
    masse = int(lines[1 + i])
    if masse_tot + masse <= 100:
        masse_tot = masse_tot + masse
    else:
        n_aller_retour += 1
        masse_tot = masse

if masse_tot > 0:
    n_aller_retour += 1

print(n_aller_retour)
