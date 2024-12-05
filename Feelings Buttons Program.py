#Felling's Button's Program by Dc117 Corp.

from tkinter import*
def bAaction():
    print('Hank You!')
def bBaction():
    print('Ouch! That hurt!')
window=Tk()
window.title('Feelings Buttons V1.10')
c=Canvas(window, width=300, height=3)
c.pack()
buttonA=Button(window, text='Press Me!', command=bAaction)
buttonB=Button(window, text='Don\'t Press!', command=bBaction)
buttonA.pack()
buttonB.pack()