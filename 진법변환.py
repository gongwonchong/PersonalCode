# a를 b로 나누고 (몫, 나머지)를 출력
def divide(a, b):
    return [a // b, a % b]

# b진법 숫자 a를 10진법으로 변경
def ToDec(a, b):
    s = list(map(int, str(a)))
    result = []
    digit = len(s) - 1
    for a in s:
        num = a * (b ** digit)
        result.append(num)
        digit -= 1
    return sum(result)

# 10진법 숫자 a를 b진법으로 변경
def FromDec(a, b):
    num = a
    result = []
    while not num < b:
        dividenum = divide(num, b)
        result.append(dividenum[1])
        num = dividenum[0]
    result.append(num)
    result.reverse()
    return int(''.join(map(str, result)))