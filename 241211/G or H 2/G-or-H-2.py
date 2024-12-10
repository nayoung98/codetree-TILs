# n명의 사람들 -> G or H
# only G or only H or G == H
# 최대 사진의 크기
# 사진의 크기 (k): 사진에서 양쪽 끝에 있는 사람 간의 거리 (사람이 1명 뿐인 경우 사진의 크기 = 0)

n = int(input())
# 사람의 위치, 알파벳 정보
tmp_list = [list(input().split()) for _ in range(n)]
info_list = [0] * 101

for idx, info in tmp_list:
    idx = int(idx)
    info_list[idx] = 1 if info == 'G' else 2

# 모든 구간의 시작점 잡기
max_len = 0
for i in range(101):
    for j in range(i + 1, 101):
        if info_list[i] == 0 or info_list[j] == 0:
            continue

        cnt_g = 0
        cnt_h = 0

        for k in range(i, j + 1):
            if info_list[k] == 1:
                cnt_g += 1
            if info_list[k] == 2:
                cnt_h += 1

        if cnt_g == 0 or cnt_h == 0 or cnt_g == cnt_h:
            leng = j - i
            max_len = max(max_len, leng)

print(max_len)        