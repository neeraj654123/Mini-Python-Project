from tkinter import *

window=Tk()

window.title("Calculater")
window.geometry("500x500")

entry=Entry(window, width=56,borderwidth=2)
entry.pack()

def click(num):
    result= entry.get()
    entry.delete(0,END)
    entry.insert(0,str(result)+str(num))


btn1=Button(window,text=1,width=12,command=lambda:click(1))
btn1.place(x=10,y=60)
btn2=Button(window,text=2,width=12,command=lambda:click(2))
btn2.place(x=130,y=60)
btn3=Button(window,text=3,width=12,command=lambda:click(3))
btn3.place(x=250,y=60)
btn4=Button(window,text=4,width=12,command=lambda:click(4))
btn4.place(x=10,y=120)
btn5=Button(window,text=5,width=12,command=lambda:click(5))
btn5.place(x=130,y=120)
btn6=Button(window,text=6,width=12,command=lambda:click(6))
btn6.place(x=250,y=120)
btn7=Button(window,text=7,width=12,command=lambda:click(7))
btn7.place(x=10,y=180)
btn8=Button(window,text=8,width=12,command=lambda:click(8))
btn8.place(x=130,y=180)
btn9=Button(window,text=9,width=12,command=lambda:click(9))
btn9.place(x=250,y=180)
btn0=Button(window,text=0,width=12,command=lambda:click(0))
btn0.place(x=130,y=240)

btn_sum=Button(window,text='+',width=12,command=lambda:add())
btn_sum.place(x=10,y=240) 
def add():
    n1=entry.get()
    global math 
    math='add'
    global i
    i=int(n1)
    entry.delete(0,END)

btn_sub=Button(window,text='-',width=12,command=lambda:sub())
btn_sub.place(x=10,y=300)

def sub():
    n1=entry.get()
    global math 
    math='sub'
    global i
    i=int(n1)
    entry.delete(0,END)

btn_mul=Button(window,text='*',width=12,command=lambda:mul())
btn_mul.place(x=250,y=240)

def mul():
    n1=entry.get()
    global math 
    math='mul'
    global i
    i=int(n1)
    entry.delete(0,END)


btn_div=Button(window,text='/',width=12,command=lambda:div())
btn_div.place(x=250,y=300)

def div():
    n1=entry.get()
    global math 
    math='div'
    global i
    i=int(n1)
    entry.delete(0,END)

btn_clear=Button(window,text='Clear',width=12,command=lambda:clear())
btn_clear.place(x=370,y=60)

def clear():
    entry.delete(0,END)

btn_equal=Button(window,text='=',width=12,command=lambda:equal())
btn_equal.place(x=130,y=300)

def equal():
    n2=entry.get()
    entry.delete(0,END)
    global math 
    if(math=='add'):
        entry.insert(0,i+int(n2))
    elif(math=='sub'):
        entry.insert(0,i-int(n2))
    elif(math=='mul'):
        entry.insert(0,i*int(n2))
    elif(math=='div'):
        entry.insert(0,i/int(n2))
    
window.mainloop()