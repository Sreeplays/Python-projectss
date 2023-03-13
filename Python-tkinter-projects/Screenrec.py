from tkinter import *
import pyscreenrec

#Configuration of the window
root = Tk()
root.geometry("800x600")
root.title("PlaysRec")
root.resizable(True, True)
root.config(bg="#2F2F4F")

#Starting of the rec configuration 
rec = pyscreenrec.ScreenRecorder()

#icons
image_icon = PhotoImage(file="D:\Sriram\Python projects\Python-tkinter-projects\Images\screen-rec.png")
root.iconphoto(False, image_icon)

#Background 

image1 = PhotoImage(file="D:\Sriram\Python projects\Python-tkinter-projects\Images\des2.png")
Label(root, image=image1, bg="#2F2F4F").place(x=350, y=30)


root.mainloop()