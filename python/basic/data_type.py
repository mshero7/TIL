# 리스트 컴프리헨션
a = [i for i in range(10) if i % 2 == 1]

print(a)

# 2차원 배열을 효율적으로 생성하는 방법
# N * M
# 반복되는 변수에 대해 무시하고 할때 _를 자주 사용하게 됨.
# array = [[0] * M for _ in range(N)]
array = [[0] * 2 for _ in range(2)]
print(array)

# 배열에서 특정 원소들을 제거하고자 할때.
# remove 함수는 하나만 제거 가능하고, 중복되더라도 하나만 제거하기에 기능적 한계
array2 = [1,2,3,4,5,5]
set1 = [2,3,5]

array3 = [i for i in array2 if i not in set1]

print(array3)

# 튜플!
# 서로 다른 성질의 데이터를 묶어서 관리해야 할 때
# 한번 선언되면 변경불가능.
# 데이터의 나열을 해싱의 키 값으로 사용해야 할때
# 리스트보다 메모리를 효율적으로 사용해야 할 때

tuple1 = (1,2,3,4,5)

print(tuple1)


# 사전 자료형!
# 키와 값을 쌍으로 가지는 자료형태.
# 키와 값의 쌍을 데이터로 가지며, 변경 불가능한 자료형을 키로 사용할 수 있다.
# ** 해시 테이블을 이용하므로 데이터의 조회 및 수정에 있어서 O(1) 시간에 처리할 수 있는 장점이 있다.

data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Bananan'
data['코코넛'] = 'Coconut'

print(data)

# 키 튜플들을 가져오게 됨
if '사과' in data:
    print("'사과'를 키로 갖는 데이터가 존재합니다.");

# 키 데이터만 담은 리스트
# keys 함수는 `dict_keys` 라는 객체를 반환하기 때문에 형변환을 진행해주어야한다.
# key_list = data.keys() (세모)
key_list = list(data.keys())
# 값 데이터만 담은 리스트
value_list = data.values()

# 집합 자료형!
# 1) 중복을 허용하지 않음 2) 순서가 없음
# 초기화 방법 
# 1) set() 함수를 활용한 초기화 2) 중괄호를 활용한 초기화( {'1','2'} )
# 데이터의 조회 및 수정에 있어서 O(1) 의 복잡도를 나타냄.
# 합,차,교집합의 연산을 제공함.
test1 = set([1, 2, 3, 4, 5])
test2 = set([3, 4, 5, 6, 7])

print(test1 | test2) # 합집합
print(test1 & test2) # 교집합
print(test1 - test2) # 차집합

# set : 관련 함수
data = set([1,2,3])
data.add(4) # 해당 원소 추가
print(data)

data.update([5,6]) # 해당 원소들 추가
print(data)

data.remove(3) # 해당 원소 삭제
print(data)

# 사전 자료형과 집합 자료형의 특징.
# 리스트나 튜플은 순서가 있기 때문에 인덱스를 통해 자료형의 값을 얻을 수 있습니다.
# 사전 자료형과 집합 자료형은 순서가 없기 때문에 인덱싱으로 값을 얻을 수 없습니다.
# 사전의 키(key) 혹은 집합의 원소(Element)를 이용해 O(1)의 시간 복잡도로 조회합니다.