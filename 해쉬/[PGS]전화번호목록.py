'''
접두어여야 함 - 시간초과
'''


def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        for j in range(i+1, len(phone_book)):
            if phone_book[i+1].startswith(phone_book[i]) == True:
                answer = False

    return answer


def solution2(phone_book):
    answer = True
    hash_map = {}  # 딕셔너리
    for phone_number in phone_book:
        hash_map[phone_number] = 1
        print("hash_map : ", phone_number, "은",
              hash_map[phone_number])  # 확인용-나중에삭제
    print("hash-map출력", hash_map)  # 확인용-나중에삭제

    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            print("temp: ", temp, "  number: ", number)  # 확인용-나중에삭제
            temp += number
            if temp in hash_map and temp != phone_number:
                # temp(key) 가 hash_map에 있고, temp가 phone_number와 다른 경우(다른 것만 비교가능하므로)
                answer = False
    return answer


phone_book = ["119", "97674223", "1195524421"]

# print(solution(phone_book))
print(solution2(phone_book))
