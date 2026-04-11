n = int(input("Matrix size (2 or 3): "))
k = [list(map(int, input().split())) for _ in range(n)]
text = input("Text: ").upper()

if len(text) % n:
    text += "X" * (n - len(text) % n)

for i in range(0, len(text), n):
    for r in range(n):
        s = sum(k[r][c] * (ord(text[i + c]) - 65) for c in range(n))
        print(chr(s % 26 + 65), end="")


# Output:
# Matrix size (2 or 3): 2
# 1 2
# 4 11
# Text: abc
# CLWB
