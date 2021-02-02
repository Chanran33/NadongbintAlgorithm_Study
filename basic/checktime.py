import time
start_time = time.time() #시간 측정

#프로그램 소스코드 ex
result=0
for i in range(5):
    result += i
    print(result)

end_time = time.time() #측정 시작
print("time: ", end_time-start_time)