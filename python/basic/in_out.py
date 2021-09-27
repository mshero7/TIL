# 자주 사용되는 표준 입력 방법.
# a = list(map(int, input().split())) # 1) 공백 기준 구분된 데이터 입력받는 방법.
# a, b, c = map(int, input().split()) # 2) 개수가 적다면 이런식으로 사용 가능.

print(a, b)

n = int(input())
data = list(map(int, input().split()))

print(data)

# sys.stdin.readline() 메서드 > 입력후 엔터키도 같이 들어오기에 rstrip() 메서드를 함께 사용. >> input 자체로도 성능이 저하될 수 있기에.. 추천
import sys
data = sys.stdin.readline().rstrip()
print(data)

# f-string 예제
answer = 7
print(f"정답은 {answer} 입니다.");

# in 연산자와 not in 연산자
# 1) list 일때는 요소의 포함여부 2) 문자열일때는 문자 하나의 포함 여부

# 조건문의 간소화.
# 1) 실행될 소스코드가 한줄인 경우, 굳이 줄바꿈 하지 않고도 간략하게 표현 가능. 2) 조건부 표현식은 if ~ else 문을 한줄에 작성할 수 있도록.

# 파이썬은 조건문 안에서 수학의 부등식을 그대로 사용 가능.
# ex) 0 < x < 20

scores = [90, 85, 77, 65, 97]
cheating_student_list = {2, 4}

for i in range(5):
    if i+i in cheating_student_list:
        continue
    elif scores[i] >= 80:
        print(f"{i+1}번째 학생은 통과")
