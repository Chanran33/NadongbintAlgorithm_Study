a = 777
print(a)

a = -5
print(a)

a=a+5
print(a)

a=a+3
print(a)

a=1e9
print(a)

#문제에서 정수형데이터를 처리한다면 오류가 발생하지 않도록 하기 위해 내장형 함수 int()를 사용하여 정수데이터로 바꾸어 처리하도록 한다.
a=int(1e9)
print(a)
#이렇게 하면 실수 연산 오차로 인한 오류를 줄일 수 있다.