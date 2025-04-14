#아스키 코드 그림 출력하기
from rich import print
from rich.console import Console
from rich.table import Table

console = Console()

def print_cat():
    cat = [
        " /\\_/\\  ",
        "( o.o ) ",
        " > ^ < "
    ]
    for line in cat:
        print(f"[yellow]{line}[/yellow]")  # 고양이 색상으로 출력

def print_bear():
    bear = [
        " ʕ•ᴥ•ʔ "
    ]
    for line in bear:
        print(f"[cyan]{line}[/cyan]")  # 곰 색상으로 출력

def print_rabbit():
    rabbit = [
        " (\\(\\ ",
        " ( -.-) "
    ]
    for line in rabbit:
        print(f"[green]{line}[/green]")  # 토끼 색상으로 출력

def show_menu():
    # 메뉴 출력에 스타일 추가
    print("[bold magenta]그림 출력 프로그램[/bold magenta]")
    print("====================")
    print("[bold]1.[/bold] [green]고양이[/green]")
    print("[bold]2.[/bold] [cyan]곰[/cyan]")
    print("[bold]3.[/bold] [yellow]토끼[/yellow]")
    print("=====================")
    print("[bold]0[/bold]을 누르면 종료됩니다\n")

def play(n):
    if n == 1:
        print("[bold green]고양이 그림을 출력합니다![/bold green]")
        print_cat()
    elif n == 2:
        print("[bold blue]곰 그림을 출력합니다![/bold blue]")
        print_bear()
    elif n == 3:
        print("[bold yellow]토끼 그림을 출력합니다![/bold yellow]")
        print_rabbit()
    else:
        print("[bold red]잘못된 입력입니다![/bold red]")

while True:
    show_menu()
    try:
        n = int(input("[bold cyan]번호를 입력하세요: [/bold cyan]"))
    except ValueError:
        print("[bold red]숫자를 입력해주세요![/bold red]")
        continue

    if n == 0:
        print("[bold magenta]프로그램을 종료합니다[/bold magenta]")
        break
    else:
        play(n)