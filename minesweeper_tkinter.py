from tkinter import *
from random import *
from datetime import datetime
import time
def destroy1():
    for slave in root.grid_slaves():
        slave.destroy()
def give_status():
    x=randrange(0,100,1)
    if(x%7==0):
        return(1)
    return(0)
def main():
    b=[]
    Label(root,text='Enter Number of rows:').grid()
    global er
    er=Entry(root)
    er.grid()
    Label(root,text="Enter Number of columns:").grid()
    global ec
    ec=Entry(root)
    ec.grid()
    Button(root,text='Submit',command=sub).grid()
def clock():
    global t
    t=t+1
    if t!='':
        label1.config(text='Timer:' +str(t))
    root.after(1000,clock)
def sub():
    global i
    i=0
    global j
    j=0
    global c
    c=int(ec.get())
    global r
    r=int(er.get())
    destroy1()
    global t
    t=0
    global label1
    label1=Label(root)
    label1.grid(row=1,)
    
    clock()
    global count
    count=0
    for i in range (r):
        b.append([])
        status.append([])
        mines.append([])
        
        for j in range(c):
            b[i].append(Button(root,text='',width=2,height=1,command= lambda idx=((c*(i))+(j)) :onclick(idx) ))
            b[i][j].grid(column=j+1,row=i+3)
            b[i][j].bind('<Button-3>',rightclick)
            status[i].append(give_status())
            mines[i].append(0)
            if(status[i][j]==1):
                count=count+1
#            print(str(status[i][j]),end=' ')
  #      print()
    check()
def rightclick(event):
    btn=event.widget
    idx=(int(str(btn)[8::])%((r*c)+2))-2
    #print(idx)
    if btn.cget("text")=="X":
        b[idx//c][idx%c].configure(text="",image='',height=1,width=2)
    else:
        b[idx//c][idx%c].configure(text="X",image=im,height=20,width=20)
def check():
    for i in range(r):
        for j in range(c):
            mine=0
            for k in range(-1,2):
                for l in range(-1,2):
                    if(i+k>-1 and j+l>-1 and i+k<r and j+l<c and ((k==0 and l==0)!=True)):
                        if(status[i+k][j+l]==1):
                            mine+=1
            #print(mine,end=' ')
            mines[i][j]=mine
        #print()
def empty(idx):
    global some
    for i in range(-1,2):
        for j in range(-1,2):
            if  ((idx//c)+i>-1 and (idx//c)+i<r and (idx%c)+j>-1 and (idx%c)+j<c and (i==j and i==0)!=True and b[i+(idx//c)][j+(idx%c)].cget("text")==''):
                b[i+(idx//c)][j+(idx%c)].configure(text=' '+str(mines[i+(idx//c)][j+(idx%c)])+' ',command=None)
                some+=1
                if mines[i+(idx//c)][j+(idx%c)]==0:
                    b[i+(idx//c)][j+(idx%c)].configure(text='   ',bg='green')
                    empty(idx+(i*c)+j)
                    
def onclick(idx):
    global some
    some+=1
        #print(some)
    #print('Status',idx,idx//c,idx%c)
    if status[idx//c][idx%c]==1:
        destroy2()
        Label(root,text='Game Over').grid()
        Button(root,text='Try Again',command=initiate).grid()
    else:
        b[idx//c][idx%c].configure(text=' '+str(mines[idx//c][idx%c])+' ',command=None)
        #print('h1',idx//c,idx%c)
        if mines[idx//c][idx%c]==0:
            b[idx//c][idx%c].configure(text='   ',bg='green')
            empty(idx)
            
    if count ==(r*c)-some:
        destroy2()
        Label(root,text='YOU WIN!!!!!!').grid()
        Button(root,text='Play Again!',command=initiate).grid()
def initiate():
    destroy1()
    global exb
    exb={}
    global mines
    mines=[]
    global b
    b=[]
    global status
    status=[]
    global some
    some=0
    main()
def destroy2():
    for i in range(r):
        for j in range(c):
            b[i][j].configure(image='',height=1,width=2)
            if status[i][j]==1:
                b[i][j].configure(text='*',command=None)
            else:
                b[i][j].configure(text=mines[i][j],command=None)
                if mines[i][j]==0:
                    b[i][j].configure(text='   ',bg='green',command=None)    
global root
root=Tk()
im=PhotoImage(file='flag.gif',height=25,width=25)
initiate()
