#import module from tkinter for UI
from tkinter import *
import os
from datetime import datetime;
#creating instance of TK
root=Tk()

root.configure(background="white")

def function1():
    
    os.system("python36 dataset_capture.py")
    
def function2():
    
    os.system("python36 training_dataSet.py")

def function3():

    os.system("python36 recognizer.py")
   
def function6():

    root.destroy()

def attend():
    os.system(os.getcwd()+"/firebase/attendance_files/attendance"+str(datetime.now().date())+'.xls')

root.title("FACE RECOGNITION BASED ATTENDANCE SYSTEM")

Label(root, text="USER INTERFACE FOR ATTENDANCE SYSTEM",font=("times new roman",20),fg="red",bg="black",height=2).grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating first button
Button(root,text="Create Dataset",font=("times new roman",20),bg="yellow",fg='black',command=function1).grid(row=3,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)

#creating second button
Button(root,text="Train Dataset",font=("times new roman",20),bg="yellow",fg='black',command=function2).grid(row=4,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating third button
Button(root,text="Recognize + Attendance",font=('times new roman',20),bg="yellow",fg="black",command=function3).grid(row=5,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating attendance sheet button
Button(root,text="Attendance Sheet",font=('times new roman',20),bg="yellow",fg="black",command=attend).grid(row=6,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)



Button(root,text="Exit",font=('times new roman',20),bg="maroon",fg="black",command=function6).grid(row=9,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)


root.mainloop()
