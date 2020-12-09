from tkinter import Frame, Label, Button, OptionMenu, Tk, StringVar, RAISED
from tkinter.colorchooser import askcolor
from VolumeLogic import ChangedValue, VolumeMixer
from SystemConnectors.WindowsConnector import WindowsConnector
# import tkinter
# print(tkinter.__file__)

class FrontEnd():

    def __init__(self, volMixer):
        self.volMixer = volMixer
        self.current_configuration = self.volMixer.applications

    def open_color_dialog(self, knob):
        # display color dialog box
        color = askcolor()
        # dont actually print just set it wherever
        self.volMixer.modify_application(knob, ChangedValue.COLOR, color[0])
        print(knob, ChangedValue.COLOR, color[0])
        return color

    def getApps(self):
        openApps = self.volMixer.getApps()
        return openApps

    def updateApp(self,knob, app):
        print(self, knob, app)
        pass

    def update(self, subject, arg):
        pass
    
    def ui_or_somethign(self):
        root = Tk()
        root.title("Bricxer")
        mainframe = Frame(root, bg='Purple')
        knobs = self.volMixer.applications
        knob = 0
        for knob in range(knobs):
            Label(mainframe, text=knob, relief=RAISED)\
                .grid(row=1, column=knob, padx=5, pady=5)
            Button(mainframe, text='Color', bg='grey', command= lambda knob: self.open_color_dialog(knob))\
                .grid(row=3, column=knob)
            options = StringVar(root)
            
            OptionMenu(mainframe, options, command= lambda knob: self.updateApp(self, knob), *self.getApps())\
                .grid(row=0, column=knob, padx=5 , pady=5)


if __name__ == '__main__':
    os_connection = WindowsConnector()
    volume_mixer = VolumeMixer(os_connection)
    f = FrontEnd(volume_mixer)
    print("why are you starting this?")
    
