import os
import webbrowser
from threading import Timer
from plyer import notification


def connect(*args):
    """This function connect to the customtkinter website incase 
    of giving the Author `Credit` or report a bug in the code
    """
    webbrowser.open_new(url='https://customtkinter.tomschimansky.com/')


def Messages(icon_name=None, title=None, message=None, timeout=None):
    try:
        if icon_name:
            icons_dir = "icons"
            icon_path = os.path.join(icons_dir, icon_name)
            return notification.notify(
                app_icon=icon_path,
                title=title,
                message=message,
                timeout=timeout
            )
    except FileNotFoundError as e:
        print('File not found', e)


import customtkinter
from PIL import Image


# class PasswordEntry(customtkinter.CTkFrame):
#     def __init__(self, master, **kwargs):
#         super().__init__(master, fg_color="transparent")

#         self.eye_open_image = customtkinter.CTkImage(Image.open("test_images/eye-password-show.png"))
#         self.eye_closed_image = customtkinter.CTkImage(Image.open("test_images/eye-password-hide.png"))

#         self.entry = customtkinter.CTkEntry(self, **kwargs, show="•")
#         self.entry.grid(row=0, column=0)

#         self.button = customtkinter.CTkButton(self, width=20, text="", image=self.eye_closed_image, command=self.button_callback)
#         self.button.grid(row=0, column=1, padx=(5, 0))

#         self.password_hide = True

#     def button_callback(self):
#         if self.password_hide:
#             self.password_hide = False
#             self.button.configure(image=self.eye_open_image)
#             self.entry.configure(show="")
#         else:
#             self.password_hide = True
#             self.button.configure(image=self.eye_closed_image)
#             self.entry.configure(show="•")


# app = customtkinter.CTk()

# password_entry = PasswordEntry(app)
# password_entry.grid(row=0, column=0, padx=20, pady=20)

# app.mainloop()