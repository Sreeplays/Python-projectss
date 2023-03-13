from tkinter import *
import pyscreenrec

#Configuration of the window
root = Tk()
root.geometry("1320x720")
root.title("PlaysRec")
root.resizable(True, True)
root.config(bg="#fff")

#Starting of the rec configuration 
rec = pyscreenrec.ScreenRecorder()

#icons
image_icon = PhotoImage(file="D:\Sriram\Python projects\Python tkinter projects\screen-rec.png")
root.iconphoto(False, image_icon)

#background 
bgimage = PhotoImage(file="Python-tkinter-projects\klue-yellow.png")
root.mainloop()