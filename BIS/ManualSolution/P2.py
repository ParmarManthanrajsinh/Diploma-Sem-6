cipher = lambda s, k: "".join(
    (
        chr((ord(c) - 65 + k) % 26 + 65)
        if c.isupper()
        else chr((ord(c) - 97 + k) % 26 + 97) if c.islower() else c
    )
    for c in s
)

text = input("Text: ")
key = int(input("Key: "))

enc = cipher(text, key)
print("Encrypted:", enc)
print("Decrypted:", cipher(enc, -key))

# Output:
# Text: abc
# Key: 123
# Encrypted: tuv
# Decrypted: abc
