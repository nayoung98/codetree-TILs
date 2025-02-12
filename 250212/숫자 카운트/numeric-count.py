# A : 1~9까지 ㅓ로 다른 숫자 세 개로 구성된 세자리 수
# B : 세 자리 수를 A에게 묻기 -> 동일한 위치: 1번 카운트 += 1, 다른 위치: 2번 카운트 += 1

# 입력
n = int(input())
info = [tuple(map(int, input().split())) for _ in range(n)]
result = []

for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if k == i or k == j:
                continue

            # 세 자리 수 구성
            answer = str(i) + str(j) + str(k)
            cnt = 0
            
            for num, a, b in info:
                # 초기화
                chk_a, chk_b = 0, 0

                # 동일 위치 확인 
                for l in range(3):
                    if str(num)[l] == answer[l]:
                        chk_a += 1

                # 존재 및 다른 위치 확인
                for l in range(3):
                    if str(num)[l] != answer[l] and str(num)[l] in answer:
                        chk_b += 1
                
                # 1번, 2번 카운트 일치 여부 확인
                if chk_a == a and chk_b == b:
                    cnt += 1
         
            if cnt == n:
                result.append(int(answer))

print(len(result))                       
