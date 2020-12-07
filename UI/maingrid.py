'''Example of how to use the grid() method to create a GUI layout'''
# import tkinter and all its functions
from tkinter import * 
from tkinter.colorchooser import *
# import IObserver

openApps = sorted([
        "master",
        "spotify",
        "chrome",
        "discord",
        "somethignElse"
        ])
knobs = [
        "knob 0",
        "knob 1",
        "knob 2",
        "knob 3",
        "knob 4"
        ]
currentConfiguration = [
        "master",
        "chrome",
        "spotify",
        "firefox",
        "firefox"
        ]
currentColors={}

def openColorDialog():
    # display color dialog box
    color = askcolor()
    print(color)
    # show the chosen RBG value
   

root = Tk() # create root window
root.title("Bricxer")
# root.maxsize(900, 600) # width x height
root.config(bg="purple")
 
# Create left and right frames
mainframe = Frame(root, bg='purple')
mainframe.grid(row=0, column=0, padx=10, pady=5)
 
# bottom_frame = Frame(root, width=650, height=400, bg='grey')
# bottom_frame.grid(row=1, column=0, padx=10, pady=5)
 
# Create frames and labels in left_frame
# Label(top_frame, text="Original Image", relief=RAISED).grid(row=0, column=0, padx=5, pady=5)
x = 0
for knob in knobs:
    Label(mainframe, text=knob, relief=RAISED).grid(row=1, column=x, padx=5, pady=5)
    Button(mainframe, text='Color', bg='grey',command=openColorDialog).grid(row=3, column=x)

    options = StringVar(root)
    options.set(currentConfiguration[x])
    OptionMenu(mainframe, options, *openApps).grid(row=0, column=x, padx=5 , pady=5)
    
    x+=1

# tool_bar = Frame(top_frame, width=180, height=185, bg='grey')
# tool_bar.grid(row=2, column=0, padx=5, pady=5)
 
def clicked():
    '''if button is clicked, display message'''
    print("Clicked.")
 
# Example labels that serve as placeholders for other widgets 
# Label(tool_bar, text="Tools", relief=RAISED).grid(row=0, column=0, padx=5, pady=3, ipadx=10)
# Label(tool_bar, text="Filters", relief=RAISED).grid(row=0, column=1, padx=5, pady=3, ipadx=10)
 
# For now, when the buttons are clicked, they only call the clicked() method. We will add functionality later. 

root.mainloop()