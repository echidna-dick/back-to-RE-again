print("keygen started")

def hash_username(name):
    v4 = 0
    for i in range(len(name)):
        c = ord(name[i])
        v9 = v4 + c * (i + 1)
        v4 = v9 ^ (v9 * 8)
        v4 = v4 & 0xFFFFFFFF

    if v4 >= 0x80000000:
        v4 = v4 - 0x100000000

    return v4

def generate_pass(username):
    h = hash_username(username)

    final = (1337 * h) ^ 23130
    final = final & 0xFFFFFFFF

    if final >= 0x80000000:
        final = final - 0x100000000
    
    return str(final)

username = input("Enter username: ")
password = generate_pass(username)
print(f"Password: {password}")
