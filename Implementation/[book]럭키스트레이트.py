score = list(map(int, input()))
half = len(score) // 2
right, left = 0, 0

for i in range(half):
    right += score[i]
for i in range(half, len(score)):
    left += score[i]
if right == left:
    print("LUCKY")
else:
    print("READY")
