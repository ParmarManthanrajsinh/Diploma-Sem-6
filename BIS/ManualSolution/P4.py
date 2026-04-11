k = input("Key: ").upper().replace("J", "I")
k = "".join(dict.fromkeys(k)) + "".join(
    c for c in "ABCDEFGHIKLMNOPQRSTUVWXYZ" if c not in k
)
m = [k[i : i + 5] for i in range(0, 25, 5)]

t = input("Text: ").upper().replace("J", "I").replace(" ", "")
p = []
i = 0
while i < len(t):
    a = t[i]
    b = t[i + 1] if i + 1 < len(t) and t[i] != t[i + 1] else "X"
    p.append(a + b)
    i += 2 if a != b else 1
if len(p[-1]) < 2:
    p[-1] += "X"

for a, b in p:
    r1, c1 = [(i, j) for i in range(5) for j in range(5) if m[i][j] == a][0]
    r2, c2 = [(i, j) for i in range(5) for j in range(5) if m[i][j] == b][0]
    if r1 == r2:
        print(m[r1][(c1 + 1) % 5] + m[r2][(c2 + 1) % 5], end="")
    elif c1 == c2:
        print(m[(r1 + 1) % 5][c1] + m[(r2 + 1) % 5][c2], end="")
    else:
        print(m[r1][c2] + m[r2][c1], end="")


# Output:
# Key: MONARCHY
# Text: HELLO
# CFSUAV
