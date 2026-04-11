p = int(input("p = "))
q = int(input("q = "))
n = p * q
phi = (p - 1) * (q - 1)

e = 2
while __import__("math").gcd(e, phi) != 1:
    e += 1

d = pow(e, -1, phi)

m = int(input("Message: "))
c = pow(m, e, n)
print("Encrypted:", c)
print("Decrypted:", pow(c, d, n))


# Output:
# p = 3
# q = 11
# Message: 7
# Encrypted: 13
# Decrypted: 7
