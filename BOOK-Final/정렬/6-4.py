# A 의 원소의 합을 최대로 만들어야 함. 최대 K번 바꿔치기
N, K = map(int, input().split())
listA = list(map(int, input().split())) 
listB = list(map(int, input().split()))

listA.sort() #오름차순
listB.sort(reverse=True) #내림차순

for i in range(K): # 최대 K번 바꿔치기 가능
    if listA[i] < listB[i]: # A의 원소가 B의 원소보다 작을 때만 바꿔주기
        listA[i] = listB[i]
    else:
        break
print(sum(listA))