def 함수명(매개변수):
    return

# global 키워드
a = 0

def func():
    global a # 이렇게 쓰면 함수내부에 참조하는것이 아닌 외부 전역변수를 가져와 참조.
    a += 1

for i in range(10):
    func()

print(a)

# 파이썬에서 함수는 여러 개의 반환 값을 가질 수 있다.
def calc(a,b):
    sum = a + b
    substract = a - b
    return sum, substract

a,b = calc(10,2)
print(f"결과값 {a} {b}")

# 람다
print((lambda a,b : a + b)(3, 7))

# 람다 표현식 예제
array = [('홍길동', 50), ('이순신', 32), ('이무개', 74)]

def my_key(x):
    return x[1]

print(sorted(array, key = my_key)) # 정렬함수로 my_key 함수를 넘겨준것.
print(sorted(array, key = lambda x: x[1])) # 정렬함수로 my_key 함수를 넘겨준것.
