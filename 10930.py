import hashlib

input_String = input()

result = hashlib.sha256(input_String.encode())

print(result.hexdigest())