import binascii

bFile = open('./text.txt', 'rb')
bData = bFile.read(1000)
print(bData)
result = ''
for ch in bData:
    result += chr(ch)
# print(result)
print(bData.decode('utf-8'))

print(binascii.hexlify(bData, " "))

b = bytearray([0x41, 0x42, 0xC3, 0x43])
print(b.decode(encoding='utf8', errors='ignore'))

a = bytes([116, 117, 118])
print(a)
