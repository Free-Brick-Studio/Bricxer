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