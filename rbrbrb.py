# rich 라이브러리에서 필요한 기능들을 가져옵니다.
from rich import print  # 내장 print 대신 rich의 print 함수를 사용합니다.
from rich.panel import Panel  # Panel 모듈은 소문자로 시작
from rich.table import Table  # Table 모듈은 제대로 호출됨
from rich.text import Text  # text 모듈도 소문자 't'로 시작

#1. 기본 print 기능 활용(색상, 스타일, 이모지)
print ("--- [bod cyan]Rich 기본출력[/bold cyal] ---")
print