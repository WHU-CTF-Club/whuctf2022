secret = [109, 96, 123, 96, 112, 99, 125, 74, 113, 86, 79, 106, 127, 116, 81, 78, 126, 117, 96, 124, 125, 113, 73, 69, 125, 111, 127, 105, 111, 120, 63, 98]

ans = ''
for i in range(0, len(secret)):
	ans = ans + chr(secret[i] ^ i)

print(ans)
