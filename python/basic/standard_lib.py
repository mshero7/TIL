# 실전에서 유용한 표준 라이브러리
# 1) itertools: 파이썬에서 반복되는 형태의 데이터를 처리하기 위한 유용한 기능들을 제공합니다. >> 순열, 조합 라이버르리는 코딩 테스트에 자주 사용됨.
# 2) heapq: 힙(Heap) 자료구조를 제공 >> 일반적으로 우선 순위 큐 기능을 구현하기 위해 사용
# 3) bisect: 이진 탐색 기능을 제공합니다.
# 4) collections: 데크(deque), 카운터(Counter) 등의 유용한 자료구조를 포함한다.
# 5) math : 필수적인 수학적 기능을 제공 >> 팩토리얼, 제곱근, 최대공약수, 삼각함수 관련 함수부터 파이(pi)와 같은 상수도 같이 포함시킴.

result = sum([1,2,3,4,5])
print(result)

min_result = min(7,3,5,2)
max_result = min(7,3,5,2)
print(min_result, max_result)

result = eval("(3+5)*7")
print(result)

# 정렬 sorted()
result = sorted([9,1,3,10,5,2])
reverse_result = sorted([9,1,3,10,5,2], reverse=True)
print(result)
print(reverse_result)

array = [('홍길동', 35), ('이순신', 20), ('문상수', 100)]
sort_array1 = sorted(array, key = lambda x : x[0])
sort_array2 = sorted(array, key = lambda x : x[1], reverse=True) # reverse 가능

print(sort_array1, sort_array2)

# 순열과 조합 (itertools)
# 1) 순열 : 서로 다른 n개에서 서로 다른 r개를 선택해서 일렬로 나열하는것. (순서를 고려함)
# 2) 조합 : 서로 다른 n개에서 순서에 상관없이 서로 다른 r개를 뽑는 경우 >> 모든 경우의 수를 고려할때 주로 사용

from itertools import combinations, permutations, combinations_with_replacement

data = ['A', 'B', 'C']

result = list(combinations(data, 2)) # 2개를 뽑는 모든 순열 구하기 (중복을 허용 하지않음, 즉 나열순서를 고려함)
print(result)

result = list(combinations_with_replacement(data,2)) # 2개를 뽑는 모든 경우의 수 구하기
print(result)

# 등장 횟수를 세는 기능 Counter
from collections import Counter
counter = Counter(['red','blue','red','green','blue','blue'])
print(dict(counter))

# math
# 나눌때 / 로 나누면 몫, 나머지 출력. // 로 몫만 출력되게끔. 
import math
def lcm(a,b):
    return a * b // math.gcd(a,b)

a = 21
b = 14

print(math.gcd(21,7))
print(lcm(21, 14))