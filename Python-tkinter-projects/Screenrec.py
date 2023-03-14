from tkinter import *
import pyscreenrec
from PIL import ImageGrab
import numpy as np
import cv2

#Configuration of the window
root = Tk()
root.geometry("800x600")
root.title("PlaysRec")
root.resizable(False, False)
root.config(bg="#2F2F4F")

#Starting of the rec configuration 
rec = pyscreenrec.ScreenRecorder()

#icons
image_icon = PhotoImage(file="D:\Sriram\Python projects\Python-tkinter-projects\Images\screen-rec.png")
root.iconphoto(False, image_icon)

#Background 

image1 = PhotoImage(file="D:\Sriram\Python projects\Python-tkinter-projects\Images\des2.png")
Label(root, image=image1, bg="#2F2F4F").place(x=-2, y=35)

#Heading 
heading = Label(root, text="PlayzRec", bg="#2F2F4F", font="arial 20 bold",)
heading.pack(pady=50)
heading.place(x=330, y=20)
heading1 = Label(root, text="(Click on the 'record' button)", bg="#2F2F4F", font="arial 10 bold",)
heading1.pack(pady=50)
heading1.place(x=306, y=75)

image3 = PhotoImage(file="D:\Sriram\Python projects\Python-tkinter-projects\Images\screen-rec.png")
Label(root, image=image3, bg="#2F2F4F").pack(pady=100)

#Buttons and its fucntions
start =  Button(root, text="Rec", bg="#fff", font="arial 15 bold", bd=0)
start.place(x=367, y=161)

root.mainloop()