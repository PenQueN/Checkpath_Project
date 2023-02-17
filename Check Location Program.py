from tkinter import * #เรียกใช้ library tkinter
from tkinter import ttk #theme of tk
from tkinter import messagebox #เรียกใช้ messagebox
import os #เรียกใช้ library os

GUI = Tk() 
GUI.title("Location Program") 
GUI.geometry('600x100+500+200') #size program (600x100) and location windows (+500+200)

def path():
    current_dir = os.getcwd() #get current path
    et1.delete(0,END) #ทำการเคลีย Textbox ก่อนการรับค่า,  0 หมายถึง index เริ่มต้นที่ตัวแรก end หมายถึงตัวสุดท้าย
    et1.insert(0,current_dir) #insert นำค่าเข้าที่ Textbox

FB1 = LabelFrame(GUI,text='Path') 
FB1.place(x=10,y=10) #Position LabelFrame

et1 = ttk.Entry(FB1,width=60) #สร้าง Textbox อยู่ภายใต้ Frame
et1.grid(row=0,column=0,padx=10,pady=10) #grid position โดยใช้ row , column สะดวกในการวางตำแหน่ง

B2 = ttk.Button(FB1,text='Browse',command=path) #สร้างปุ่ม Button อยู่ภายใต้ Frame
B2.grid(row=0,column=1,padx=10,pady=10) #padx , pady ใช้สำหรับ frame

GUI.mainloop() #วนทำงานไปเรื่อย ๆ

