# 구구단 프로그램
def multiplication_table(n):
    print(f"== {n}단 ==")
    for i in range(1, 10):
        print(f"{n} x {i} = {n*i}")

# 사용자 입력 받기
try:
    num = int(input("몇 단을 출력할까요? "))
    multiplication_table(num)
except ValueError:
    print("숫자를 입력해주세요.")
    