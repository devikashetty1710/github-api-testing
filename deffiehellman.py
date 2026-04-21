# input keys
p = int(input("Enter prime number (p): "))
g = int(input("Enter primitive root (q): "))

# private keys
a = int(input("Enter alice's private key: "))
b = int(input("Enter bob's private key: "))

# public keys
A = pow(g, a, p)
B = pow(g, b, p)

print("Alice's public key: ", A)
print("Bob's public key: ", B)

# shared key
secret_a = pow(B, a, p)
secret_b = pow(A, b, p)

print("Alice's secret key: ", secret_a)
print("Bob's secret key: ", secret_b)

if secret_a == secret_b:
    print("Shared secret key established successfully")

    