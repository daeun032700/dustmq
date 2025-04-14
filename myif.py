#아스키 코드 그림 출력하기
def print_cat():
    cat = [
        " /\\_/\\  ",
        "( o.o ) ",
        " > ^ < "
    ]
    for line in cat:
        print(line)

def print_bear():
    bear = [
        " ʕ•ᴥ•ʔ "
    ]
    for line in bear:
        print(line)

def print_rabbit():
    rabbit = [
        " (\\(\\ ",
        " ( -.-) "
    ]
    for line in rabbit:
        print(line)
def show_menu():
    print("그림 출력 프로그램")
    print("====================")
    print("1. 고양이")
    print("2. 곰")
    print("3. 토 끼")
    print("=====================")
    print("0을 누르면 종료됩니다")

    # 만약에 1을 입력하면 1번 캐릭터 출력
def play(n):
    if n == 1:
        print("고양이")
        print_cat()
    # 만약에 2를 입력하면 2번 캐릭터 출력
    elif n == 2:
        print("곰")
        print_bear()
    # 만약에 3을 입력하면 3번 캐릭터 출력
    elif n == 3:
        print("토끼")
        print_rabbit()
    # 잘못입력하면 잘못 입력했다고 출력
    else:
        print("잘못입력")
#할 수 있는 사람은 프로그램이 계속(무한)반복하게 하고
while True:
    show_menu()
    try:
        n = int(input("번호를 입력하세요: "))
    except ValueError:
        print("숫자를 입력해주세요!")
        continue

    if n == 0:
        print("프로그램을 종료합니다")
        break
    else:
        play(n)
#만약에 0을 입력하면 종료되는 프로그램을 만드시오
