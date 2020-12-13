from tkinter import Frame, Label, Button, OptionMenu, Tk, StringVar, RAISED
from tkinter.colorchooser import askcolor
from VolumeLogic import ChangedValue, VolumeMixer
from SystemConnectors import WindowsConnection
from functools import partial


class FrontEnd:
    """Handles the Settings UI"""
    
    def __init__(self, volume_mixer):
        """
        Initializes FrontEnd

        :param volume_mixer: Volume Mixer used to communicate with rest of application
        """
        self._volume_mixer = volume_mixer

    def open_color_dialog(self, knob):
        """
        Opens color picker and passes selected color to Volume Mixer

        :param knob: Knob number
        """
        color = [int(x) for x in askcolor()[0]]
        self._volume_mixer.modify_application(knob, ChangedValue.COLOR, color)

    def get_apps(self):
        """
        Gets apps for dropdown, occurs every time dropdown is opened

        :return: list of app names with last 4 characters removed
        """
        return self._volume_mixer.get_running_applications()
    
    def update_app(self, knob, app_name):
        """
        Sends app seleced from dropdown to volumemixer, tied with knob

        :param knob Knob number 
        :param app_name: name of selected app
        """
        self._volume_mixer.set_application(knob, app_name)
    
    def launch(self):
        """
        Launches UI
        """
        root = Tk()
        root.title("Bricxer")
        main_frame = Frame(root, bg='Purple')
        main_frame.grid(row=0, column=0, padx=10, pady=5)
        
        for index, app in enumerate(self._volume_mixer.applications):
            Button(main_frame, text='Color', bg='Grey', 
                command=partial(self.open_color_dialog, index)) \
                .grid(row=3, column=index)
            
            Label(main_frame, text=index) \
                .grid(row=1, column=index, padx=5, pady=5)

            option = StringVar(root)
            option.set("None Set") if app==None else option.set(app.name)
                

            OptionMenu(main_frame, option, 
                command=partial(self.update_app, index), *self.get_apps()) \
                .grid(row=0, column=index, padx=5 , pady=5)
        root.mainloop()
    
if __name__ == '__main__':
    os_connection = WindowsConnection()
    volume_mixer = VolumeMixer(os_connection)
    FrontEnd(volume_mixer).launch()
