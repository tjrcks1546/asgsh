#입력은 v = 숫자배열을 입력값으로 받는다
#v의 길이 구하기= len

# 0번째과 1번째 수 비교하기
# v[0] <v[1] 이면
# max = v[1] 저장
# max <v[2] 이면
# max = v[2]
# max < v[3] 이면,
# max = v[3]



def max_value (v):
    length = len(v)
    max = v[0]
    for i in range (0,length):
        if max < v [i]:
            max = v[i]
        else:
            max = max
    return max    

            

