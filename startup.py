"""These are built-in modules, which are part of the Python standard library"""
from tkinter import *

"""These are third-party modules that need to be installed separately using pip"""
import customtkinter

"""This are local modules created by me and are part of the project"""
from home.homepage import Homepage
from app_image_utils.image_utils import get_ctk_image


class Loading():

    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('green')

    def __init__(self):

        WIDTH: int = 540
        HEIGHT: int = 400
        
        self.main_window = customtkinter.CTk()
        self.main_window.resizable(0, 0)
        self.main_window.minsize(500, 400)
        self.main_window.title('Loading')
        
        self.main_window.attributes('-topmost', True)
        self.main_window.after(500, self.main_window.deiconify)
        self.main_window.geometry(f'{WIDTH}x{HEIGHT}+414+160')

        """This script is used to configure the main_window"""
        self.main_window.columnconfigure(0, weight=1)
        self.main_window.rowconfigure(0, weight=1)


        self.progress_logo = customtkinter.CTkLabel(master=self.main_window, text="", 
                                                    image=get_ctk_image(icon='logo_05', 
                                                                        size=200))
        self.progress_logo.grid(row=0, column=0, padx=20, pady=20)


        self.progress_label = customtkinter.CTkLabel(master=self.main_window, text='', 
                                                     font=('Sans', 16))
        self.progress_label.grid(row=1, column=0, sticky=NSEW)


        self.progress_bar = customtkinter.CTkProgressBar(master=self.main_window, width=480, 
                                                         border_width=1, height=15,
                                                         mode='determinate', corner_radius=7, orientation='horizontal',
                                                         determinate_speed=2, progress_color='#16FF00')
        self.progress_bar.grid(row=2, column=0, padx=20, pady=20, sticky=EW)
        self.progress_bar.set(0.0)


    counter = 0

    def loading_progress_bar(self, value) -> None:
        """This function loads the page!! Refer to (README2.md in the package folder) """
        self.progress_bar.set(value)
        if self.counter <= 10:
            test = 'Please wait, while we load your homepage ....[' + \
                   (str(10 * self.counter) + '%]')
            self.progress_label.configure(text=test)
            self.progress_bar.after(1000, self.loading_progress_bar, value + 1 / 10)
            self.counter += 1
        else:
            self.main_window.withdraw()
            Homepage(self.main_window)
            self.main_window.withdraw()

    def run(self) -> None:
        self.loading_progress_bar(0)
        self.main_window.mainloop()

if __name__ == '__main__':
    app = Loading()
    app.run()

