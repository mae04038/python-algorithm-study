# 균형잡힌 문자열인지 확인 : '('')'개수 같아야 함.
def isBalanced(s):
    chk = 0
    for c in s:
        if c == '(':
            chk += 1
        elif c == ')':
            chk -= 1
    if chk == 0:
        return True
    else:
        return False

# 올바른 괄호 문자열인지 확인 : 개수 같고 짝도 맞아야 함.
# 괄호가 열릴 때마다 스택에 넣고 괄호가 닫힐 때마다 스택에서 빼기.


def isCorrect(s):
    stack = []
    stack.append(s[0])
    for i in range(1, len(s)):
        if len(stack) == 0 or stack[-1] == ')' or (stack[-1] == '(' and s[i] == '('):
            stack.append(s[i])
        else:
            stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False


def solution(p):
    answer = ''
    u = ""  # 균형잡힌 문자열 저장
    v = ""  # 빈 문자열 저장
    # 빈 문자열이거나 올바른 괄호 문자열은 그대로 리턴
    if len(p) == 0 or isCorrect(p):
        return p

    # u가 균형잡힌 문자열이 될 때까지 2개씩 추가해서 u, v 나누기
    for i in range(2, len(p)+1, 2):
        if isBalanced(p[0:i]):
            u = p[0:i]
            v = p[i:len(p)]
            break
    if isCorrect(u):
        # u가 올바른 괄호 문자열일 때 - 3단계 수행
        answer += u + solution(v)
    else:
        # u가 올바른 괄호 문자열이 아닐 때 - 4단계 수행
        answer += '(' + solution(v) + ')'
        for c in u[1:-1]:
            if c == '(':  # 뒤집어서ㅓ 붙이기
                answer += ')'
            else:
                answer += '('

    return answer
