import tkinter as tk

class App(tk.Frame):
    
    def __init__(self, master=None):

        openApps = [
            "master",
            "spotify",
            "chrome",
            "discord",
            "somethignElse"
        ]
        knobs = [
            "master",
            "spotify",
            "chrome",
            "discord",
            "somethignElse"
        ]
        gridElements = {}
        x = 0
        for knob in knobs:
            gridElements[knob] = tk.Label(master,)
            
        grid = tk.Grid
        super().__init__(master)
        self.pack()

# create the application
myapp = App()

#
# here are method calls to the window manager class
#
myapp.master.title("My Do-Nothing Application")
myapp.master.minsize(100, 400)

# start the program
myapp.mainloop()