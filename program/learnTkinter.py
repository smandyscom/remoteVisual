from tkinter import *
import tkinter
root = Tk()
#some = Label(root, text="Tk's job!!", width="30", height="5")
some = Text(root , height=5,width=30)
some.pack()
some.insert(END,"aloha")
