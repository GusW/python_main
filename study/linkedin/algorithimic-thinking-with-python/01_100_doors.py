doors = [False] * 100

"""
0    F F F F F F F F F F
1    T T T T T T T T T T
2    T F T F T F T F T F
3    T F F F T T T F F F
4    T F F T T T T T F F
5    T F F T F T T T F T
6    T F F T F F T T F T
7    T F F T F F F T F T
8    T F F T F F F F F T
9    T F F T F F F F T T
10   T F F T F F F F T F

"""

for i in range(len(doors)):
    for j in range(i, len(doors), i + 1):
        doors[j] = not doors[j]


for idx, d in enumerate(doors, 1):
    if d:
        print(idx, end=", ")

print("\n")
