from Tkinter import Tk, Frame, BOTH, StringVar, Entry, Label, Radiobutton
import Tkinter
from PIL import Image, ImageTk

class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("PISE")
        self.pack(fill=BOTH, expand=1)

root = Tk()
root.geometry("1111x675")
app = Example(root)

im = Image.open('images/leatherBackground.png')
im = im.resize((1200,800), Image.BILINEAR)
tkimage = ImageTk.PhotoImage(im)
myvar=Tkinter.Label(root,image = tkimage)
myvar.place(x=0, y=0, relwidth=1, relheight=1)

custName = StringVar()
yourName = Entry(root, textvariable=custName)
yourName.pack()

relStatus = StringVar()
relStatus.set(None)

labelText = StringVar()
labelText.set('Accuracy Level')
label1 = Label(root, textvariable=labelText, height=2)
label1.pack()

def beenClicked1():
    pass

def beenClicked5():
    pass


root.mainloop()