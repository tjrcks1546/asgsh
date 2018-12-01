#팩토리얼 재귀함수로 구하기
#n!=n*n-1
#n= n * n -1
#n<1 마이너스 팩토리얼은 구할수가 없다.
#n==1 땐 1을 출력
#n>1뗀 n*factorial(n-1)
#팩토리얼 함수를 다시 불러와서 n-1씩 낮아지게 함수를 다시 불러옴 
def factorial(n):
    if n<0:
        print('팩토리얼은 마이너스를 구할수없습니다.')
    if n == 0:
        return 1
    if 0<n<=992:#최대 992까지의 팩토리얼을 구할수 있네요
        return n*factorial(n-1)
    if n > 992:
        print("Infinity")
    
