from tkinter import Frame, Label, Button, OptionMenu, Tk, StringVar, RAISED
from tkinter.colorchooser import askcolor
from VolumeLogic import ChangedValue, VolumeMixer
from SystemConnectors import WindowsConnection
from functools import partial


class FrontEnd():
    """Handles the Settings UI"""
    
    def __init__(self, volume_mixer):
        """
        Initializes FrontEnd
        :param volume_mixer: Volume Mixer used to communicate with rest of application
        """
        self.volume_mixer = volume_mixer
        self.current_configuration = self.volume_mixer.applications
        self.open_apps = self.volume_mixer.get_running_applications()

    def open_color_dialog(self, knob):
        """
        Opens color picker and passes selected color to Volume Mixer
        :param knob: Knob number
        """
        color = askcolor()[0]
        color = [int(x) for x in color]
        print(knob, color)
        self.volume_mixer.modify_application(knob, ChangedValue.COLOR, color)

   
    def get_apps(self):
        """
        Gets apps for dropdown, occurs every time dropdown is opened
        :return: list of app names with last 4 characters removed
        """
        self.open_apps = self.volume_mixer.get_running_applications()
        return [app.name[0: -4] for app in self.open_apps]

    
    def update_app(self, knob, app_name):
        """
        Sends app seleced from dropdown to volumemixer, tied with knob
        :param knob Knob number 
        :param app_name: name of selected app
        """
        for i in self.open_apps:
            if(i.name.find(app_name)):
                app = i
                break
        self.volume_mixer.set_application(knob, app)
        print(knob, app)
  
    
    def launch(self):
        """
        Launches UI
        """
        root = Tk()
        root.title("Bricxer")
        main_frame = Frame(root, bg='Purple')
        main_frame.grid(row=0, column=0, padx=10, pady=5)
        
        knobs = self.volume_mixer.applications
        for knob in range(len(knobs)):
            Label(main_frame, text=knob).grid(row=1, column=knob, padx=5, pady=5)

            Button(main_frame, text='Color', bg='Grey', \
                command=partial(self.open_color_dialog, knob)) \
                .grid(row=3, column=knob)
            
            option = StringVar(root)
            option.set("Empty")
            OptionMenu(main_frame, option, \
                command=partial(self.update_app, knob), *self.get_apps()) \
                .grid(row=0, column=knob, padx=5 , pady=5)
        root.mainloop()
    
if __name__ == '__main__':
    os_connection = WindowsConnection()
    volume_mixer = VolumeMixer(os_connection)
    ui = FrontEnd(volume_mixer)
    ui.launch()
