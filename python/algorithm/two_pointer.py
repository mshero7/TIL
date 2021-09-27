n, m = 6, 5
data = [1,5,2,3,2,5];

result = 0
summary = 0
end = 0

for start in range(n):
    while summary < m and end < n :
        summary += data[end]
        print(f"start : {start} end : {end} summary : {summary}")
        end += 1
    print('1234')
    if summary == m :
        result += 1
        print(f"start : {start} end : {end} summary : {summary} result : {result}")
    summary -= data[start]

print(result)

# 투포인터.
# 리스트에 순차적으로 접근해야 할때 두 개의 점 위치를 기록하면서 처리하는 알고리즘.
# 문제) 길이가 6인 배열에서 구간합이 5인 구간은 총 몇개인지 구하라.
# 생각))
# 1) 구간이란것이 있으니 시작과 끝을 어떻게 처리할것인지 생각.
# 2) start 를 첫 for문에 넣고 end 는 확장되게끔, 구간합을 정리하면서 다음 start 시에 구간합 - 이전 배열[start].

n, m = 6, 5
data = [1,5,2,3,2,5];

start = 0
end = 0
sum = 0
result = 0

for start in range(n):
    if(sum == m):
        result += 1
    else:
        while(end < n and sum < m):
            sum += data[end]
            end += 1
    sum -= data[start]

