# 수의 크기 비교, 숫자를 거꾸로 읽는다.
# 두 수가 주어졌으 때, 상수의 대답 출력 프로그램

# 첫째 줄에 두 수 A와 B -> 같지않은 세 자리수, 0 포함x
# 첫째 줄에 상수의 대답 출력

A, B = input().split()
A = int(A[::-1])
B = int(B[::-1])

if A > B :
    print(A)

else :
    print(B)
