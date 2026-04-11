r = int(input("Rows: "))
t = input("Text: ")
f = [""] * r
i = 0
d = 1
for c in t:
    f[i] += c
    if i == 0:
        d = 1
    elif i == r - 1:
        d = -1
    i += d
print("".join(f))

# Output:
# Rows: 3
# Text: HELLO
# HOELL
