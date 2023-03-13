from tkinter import *
import pyscreenrec

#Configuration of the window
root = Tk()
root.geometry("400x600")
root.title("PlaysRec")
root.resizable(True, True)
root.config(bg="#fff")

#Starting of the rec configuration 
rec = pyscreenrec.ScreenRecorder()

#icons
image_icon = PhotoImage(file="D:\Sriram\Python projects\Python-tkinter-projects\Images\stop-button.png")
root.iconphoto(False, image_icon)

#Background 

image1 = PhotoImage(file="D:\Sriram\Python projects\Python-tkinter-projects\Images\des2.png")
Label(root, image=image1, bg="#fff").place(x=0, y=0)
root.mainloop()