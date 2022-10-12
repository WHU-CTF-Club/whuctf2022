import base64

code = [
	0x4A, 0x27, 0x4F, 0x3A, 0x4A, 0x19, 0x1D, 0x16, 
	0x4F, 0x26, 0x3B, 0x45, 0x4C, 0x3D, 0xD8, 0x21, 
	0x48, 0x4B, 0x29, 0x49, 0x4F, 0x18, 0x29, 0x3A,
	0x4C, 0x3D, 0xD8, 0x23, 0x44, 0x17, 0x4B, 0x36, 
	0x44, 0xE0, 0x24, 0x4B, 0x4B, 0x3F, 0xD4, 0xD4,
]

# ch = static_cast<char>((ch ^ 191) + 9810)
data = ''
for ch in code:
	data += chr(((ch + 174) % 256) ^ 191)

oldtable = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
newtable = ''
for ch in oldtable:
    newtable += chr(ord(ch) + 1)
    
print(newtable)

bdata = base64.b64decode(data.translate(data.maketrans(newtable, oldtable)))

# ch = static_cast<char>((ch ^ 114) + 514)
ans = ''
for ch in bdata:
    ans += chr(((ch + 254) % 256) ^ 114)

print(ans)
