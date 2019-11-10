""" Pour résoudre ce problème il est nécessaire de prendre le premier sous_mot
et de ce premier mot le découper en tous les sous_mots réalisable avec celui-ci
une fois que l'on a tous les sous mots possibles on regarde le plus long à l'intérieur
de tous les strings"""

import sys

N_word = int(input())

lines = []
for line in sys.stdin:
    lines.append(line.rstrip("\n"))


def contains(s1, s2):
    """ Returns True if s1 is in s2 """

    if s1 == "":
        return True
    elif s2 == "":
        return False
    else:
        if s1[0] == s2[0]:
            return contains(s1[1:], s2[1:])
        else:
            return contains(s1, s2[1:])


def sous_mots(m):
    if m == "":
        return [""]
    else:
        aux = sous_mots(m[1:])
        res = []
        for e in aux:
            res.append(m[0] + e)
        return res + aux


result = ""
test_line = lines[0]
sous_mots = sous_mots(test_line)

for sous_mot in sous_mots:
    exist = True
    for line in lines:
        if not contains(sous_mot, line):
            exist = False
    if exist and len(sous_mot) > len(result):
        result = sous_mot


if result == "":
    print("KO")
else:
    print(result)
