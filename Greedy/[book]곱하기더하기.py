s = list(map(int, input()))  # 문자열 S

result = s[0]

for i in range(1, len(s)):
    if result == 0:
        result += s[i]
    elif s[i] != 0 and result != 0:
        result *= s[i]

print(result)
