import sys

input = sys.stdin.readline
m1, d1, m2, d2 = map(int, input().split())
A = input().rstrip()

# 요일 인덱스 매핑
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
target_day_index = days.index(A)

# 2024년의 각 월별 일수 설정
month_days = [0, 31, 29, 31, 30, 31, 30, 31, 30, 31, 30, 31]

# 현재 요일 인덱스 초기화
current_day_index = 0  # 2024년 1월 1일은 월요일

# 특정 요일 카운트
count = 0

# 시작 날짜부터 끝 날짜까지 반복
while not (m1 == m2 and d1 == d2 + 1):  # m2월 d2일을 포함하기 위해 d1은 d2 + 1보다 작아야 함
    # 목표 요일인지 확인
    if current_day_index == target_day_index:
        count += 1

    # 날짜 증가
    d1 += 1
    current_day_index = (current_day_index + 1) % 7  # 다음 요일로 변경

    # 다음 날이 해당 월의 마지막 날이면 월을 증가
    if d1 > month_days[m1]:
        d1 = 1
        m1 += 1

# 결과 출력
print(count)