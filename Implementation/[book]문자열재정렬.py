s = list(input())
alphabet = []
digits = []
for data in s:
    if data.isalpha() == True:
        alphabet.append(data)
    else:
        digits.append(int(data))
alphabet.sort()

for i in alphabet:
    print(i, end="")
print(sum(digits))
