# tkinter

from tkinter import *
import pandas as pd
import os

print(os.getcwd())

dat = pd.read_csv("./law.csv", encoding='euc-kr') #한국어 인코딩 바꾸기

print(dat.columns)

def click():
  word = entry.get()
  output.delete(0.0, END)

  try:
      def_word=dat.loc[dat['용어명'] == word, '설명'].values[0]
  except:
      def_word = "단어의 뜻을 찾을 수 없음."

  output.insert(END, def_word)


window = Tk()
window.title("My Dictionary")

label = Label(window, text="원하는 단어 입력 후, 엔터 키 누르기")
label.grid(row=0, column=0, sticky=W)

# 02 텍스트 입력이 가능한 상자(Entry)
entry = Entry(window, width=15, bg="light green")
entry.grid(row=1, column=0, sticky=W)

# 03 제출 버튼 추가
button = Button(window, width=5, text="검색", bg="gray", command=click) #윈도우 안에 넣을거다...
button.grid(row=2, column=0, sticky=E)

#btn = Button(window, text="제출", width=5, command=click)
#btn.grid(row=2, column=0, sticky=W)

# 04 설명 레이블 - 의미
lable2 = Label(window, text="\n설명:")
lable2.grid(row=3, column=0, sticky=W)

# 05 텍스트 박스 입력 상자
# columnspan=2 는 (4,0)~(4,1) 위치까지 분포
output = Text(window, width=50, height=6, wrap=WORD, background="light green")
output.grid(row=4, column=0, columnspan=2, sticky=W)

# 메인 반복문 실행
window.mainloop()