import tkinter as tk
from tkinter import messagebox, END
import tkinter.scrolledtext as scrolledtext
import tkinter.ttk
import random

con = 0

#주사위로 알아보기 함수
def Pdice(): 
    
    #displayText 초기화
    displayText.delete('1.0', END)
    displayText.update()

    #변수들
    preCount = enterValue.get()
    preSelect = enterValueForDc.get()
    count = int(preCount)
    select = int(preSelect)
    stock = list()

    for i in range(1, count+1):  #반복 시행
        dice = random.randrange(1, 7)
        stock.append(dice)
        displayText.insert(tk.END, int(i))
        displayText.insert(tk.END, '회 →')
        displayText.insert(tk.END, int(dice))
        displayText.insert(tk.END, '\n')
    
    #메세지 박스로 결과출력
    result = select, '이(가)', '나올', '확률은', stock.count(select)/count, '입니다'
    messagebox.showinfo('result', result)

# 동전으로 알아보기 함수
def Pcoin():  
    
    #displayText 초기화
    displayText.delete('1.0', END)
    displayText.update()

    #변수들
    preCount = enterValue.get()
    count = int(preCount)
    stock = list()
    
    for i in range(1, count+1):   #반복 시행
        coin = random.randrange(0, 2)
        stock.append(coin)
        if coin == 0:
            displayText.insert(tk.END, int(i))
            displayText.insert(tk.END, '회 → H')
            displayText.insert(tk.END, '\n')

        elif coin == 1:
            displayText.insert(tk.END, int(i))
            displayText.insert(tk.END, '회 → T')
            displayText.insert(tk.END, '\n')
    
    #메세지 박스로 결과출력
    result = '앞면이', '나올', '확률은', stock.count(0)/count, '입니다'
    messagebox.showinfo('result', result)


#도움말 함수
def help():
    advice = '''
    통계적 확률을 알아보고자 동전이나 주사위를 던집니다.
    ★ 동전에서 앞면과 뒷면이 나올 확률은 각각 0.5 입니다.
    ★ 주사위에서 각 눈이 나올 확률은 약 0.1666667 입니다.
    적당히 큰 수를 설정하시고 위의 값과 비슷한지 확인해보세요.
    ※동전은 앞면만 취급합니다※
    '''
    messagebox.showinfo('도움말', advice)
    
#횟수 입력 엔트리 자동삭제 함수
def autoDel0(event):
    enterValue.delete(0, 100)

#눈 입력 엔트리 자동삭제 함수
def autoDel1(event):
    enterValueForDc.delete(0, 100)

#프로그램 정보 함수
def info():
    appInfo =''' 버전 1.02, 제작: 임영훈'''
    messagebox.showinfo('프로그램 정보', appInfo)

#같이 종료 함수
def destroyAll():
    percent.destroy()
    if con==1:
        pass
    else:
        display.destroy()

# '같이 종료' 함수를 위한 con에 값을 주는 함수
def connectionX():
    global con
    con = 1
    display.destroy()

# 디스플레이 다시 띄우기 버튼 함수
def reImportDisplay():
    global con
    if con == 1:
        
        con =0
        #디스플레이 창
        global display
        display = tk.Tk()
        display.title('모니터')
        display.geometry('550x350+200+100')
        display.resizable(False, False)
        
        #디스플레이 텍스트
        global displayText
        displayText = tk.Text(display
        , width='70'
        , relief='groove')
        displayText = scrolledtext.ScrolledText(display, undo=True)
        displayText.pack(pady='30')

        percent.protocol('WM_DELETE_WINDOW', destroyAll)
        display.protocol('WM_DELETE_WINDOW', connectionX)
        display.mainloop()

#메인 윈도우 시작
percent = tk.Tk()
percent.title('실행기')
percent.geometry('280x390+800+100')
percent.resizable(False, False)

#타이틀
title = tk.Canvas(percent
, width = 240
, height = 50)
title.pack(pady='10')

title.create_rectangle(2,2,237,50)
title.create_text(120, 25
, text = "Statistical Probability"
, font=('Times', 15))

#코인버튼
btnCoin = tk.Button(percent
, text='동전으로 알아보기'
, width = '32'
, command = Pcoin
, height='2'
, bg ='lightcyan'
, overrelief='groove'
, activebackground='light blue'
, state='normal')
btnCoin.pack(pady = '10')

#주사위버튼
btnDice = tk.Button(percent
, text='주사위로 알아보기'
, width = '32'
, height='2'
, command=Pdice
, bg='lightcyan'
, overrelief='groove'
, activebackground='light blue')
btnDice.pack(pady = '10')

#구분
sep2 = tk.Label(percent
, text='────────────────────────────')
sep2.pack()

#시행 횟수 입력
accountForCnt = tk.Label(percent
, text='시행 횟수')
accountForCnt.pack()
    
    #시행 횟수 입력: 엔트리
enterValue = tk.Entry(percent
, width = '30')
enterValue.insert(1, '먼저 입력하시고 버튼을 눌러주세요')
enterValue.bind('<Button-1>', autoDel0)
enterValue.pack()

#구분
sep2 = tk.Label(percent
, text='')
sep2.pack()


#주사위 눈 입력
accountForDc = tk.Label(percent
, text='주사위의 눈 선택 (주사위를 선택할때)')
accountForDc.pack()
    
    #눈 입력: 엔트리
enterValueForDc = tk.Entry(percent
, width = '5')
enterValueForDc.insert(0, '(1~6)')
enterValueForDc.bind('<Button-1>', autoDel1)
enterValueForDc.pack()
    
#구분
sep3 = tk.Label(percent, text='────────────────────────────')
sep3.pack()

#도움말
help0 = tk.Button(percent
, bitmap='question'
, width='45'
, height='30'
, overrelief='groove'
, command = help
, bg='snow'
, activebackground='old lace')
help0.place(x='35', y='340')

#프로그램 정보
information = tk.Button(percent
, bitmap='info'
, width='45'
, height='30'
, overrelief='groove'
, command = info
, bg='snow'
, activebackground='old lace')
information.place(x='115', y='340')

#디스플레이 다시 띄우기
reImportDisplayBtn = tk.Button(percent
, bitmap='gray50'
, width='45'
, height='30'
, overrelief='groove'
, command = reImportDisplay
, text='모니터'
, bg='snow'
, activebackground='old lace')
reImportDisplayBtn.place(x='195', y='340')

#디스플레이 창
display = tk.Tk()
display.title('모니터')
display.geometry('550x350+200+100')
display.resizable(False, False)

#디스플레이 텍스트
displayText = tk.Text(display
, width='70'
, relief='groove')
displayText = scrolledtext.ScrolledText(display, undo=True)
displayText.pack(pady='30')


percent.protocol('WM_DELETE_WINDOW', destroyAll)
display.protocol('WM_DELETE_WINDOW', connectionX)
display.mainloop()
percent.mainloop()