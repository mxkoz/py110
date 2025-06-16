import random

def UUID():
    UUID_chars = '0123456789abcdefghijklmnoqrstuvwxyz'
    UUID = ['']
    for _ in range(0,32):
        UUID += UUID_chars[random.randint(0,34)]
    return ''.join(UUID)

print(UUID())