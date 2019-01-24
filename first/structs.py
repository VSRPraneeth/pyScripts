from struct import *

# Stores as bytes data

packed_data = pack('iif', 6, 19, 4.26)
print(packed_data)

print(calcsize('i'))
print(calcsize('f'))
print(calcsize('iif'))

# To get byte data

original_data = unpack('iif', packed_data)

print(original_data)
print(unpack('iif', b'\x06\x00\x00\x00\x13\x00\x00\x00\xecQ\x88@'))