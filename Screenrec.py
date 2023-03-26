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
root.config(bg="#969696")

def start_rec():
    file = Filename.get()
    rec.start_recording(str(file+'.mp4'),5)

def pause_rec():
    rec.pause_recording()
def stop_rec():
    rec.stop_recording()
def resume_rec():
    rec.resume_recording()


#Starting of the rec configuration 
rec = pyscreenrec.ScreenRecorder()

#icons
image_icon = PhotoImage(file="D:\Sriram\Python projects\Python-tkinter-projects\Dist\Images\screen-rec.png")
root.iconphoto(False, image_icon)

#Background 

image1 = PhotoImage(file="D:\Sriram\Python projects\Python-tkinter-projects\Dist\Images\yelllow1.png")
Label(root, image=image1, bg="#969696").place(x=-2, y=20)
image =  PhotoImage(file=r"D:\Sriram\Python projects\Python-tkinter-projects\Dist\Images\blue.png")
Label(root, image=image, bg="#969696").place(x=635, y=400)
#Heading 
heading = Label(root, text="PlayzRec", bg="#969696", font="arial 20 bold",)
heading.pack(pady=50)
heading.place(x=330, y=20)
heading1 = Label(root, text="(Click on the 'record' button)", bg="#969696", font="arial 10 bold",)
heading1.pack(pady=50)
heading1.place(x=303, y=75)
#Heading image
image3 = PhotoImage(file="D:\Sriram\Python projects\Python-tkinter-projects\Dist\Images\screen-rec.png")
Label(root, image=image3, bg="#969696").pack(pady=100)

#entry
Filename = StringVar()
entry = Entry(root, textvariable=Filename, width=30, font="Helvetica 13")
entry.place(x=235, y= 315)
Filename.set("recorded1")
filenametext = Label(root, text="(Set your 'filename'.mp4)", bg="#969696", font="Helvetica 10 bold")
filenametext.pack(pady=50)
filenametext.place(x=300, y=345)

#Buttons and its fucntions
start =  Button(root, text="Rec", bg="#fff", font="arial 15 bold", bd=0, command=start_rec)
start.place(x=367, y=161)
#PAUSE
image4 = PhotoImage(file="D:\Sriram\Python projects\Python-tkinter-projects\Dist\Images\pause.png")
pause = Button(root, image=image4, bg="#969696", bd=0, command=pause_rec)
pause.place(x=80, y=450)
pausetext = Label(root, text="Pause", font="Helvetica 10 bold", bd=0, bg="#969696")
pausetext.pack(pady=20)
pausetext.place(x=95, y=530)
#RESUME
image5 = PhotoImage(file=r"D:\Sriram\Python projects\Python-tkinter-projects\Dist\Images\unpause.png")
resume = Button(root, image=image5, bg="#969696", bd=0, command=resume_rec)
resume.place(x=350, y=450)
resumetext = Label(root, text="Pause", font="Helvetica 10 bold", bd=0, bg="#969696")
resumetext.pack(pady=20)
resumetext.place(x=365, y=530)
#STOP
image6 = PhotoImage(file="D:\Sriram\Python projects\Python-tkinter-projects\Dist\Images\stop.png")
stop = Button(root, image=image6, bg="#969696", bd=0, command=stop_rec)
stop.place(x=585, y=450)
stoptext = Label(root, text="Stop", font="Helvetica 10 bold", bd=0, bg="#969696")
stoptext.pack(pady=20)
stoptext.place(x=615, y=530)


root.mainloop()