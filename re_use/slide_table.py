from tkinter import *
import customtkinter
from random import choice


# class AnimateWindow():
#     def __init__(self, window):
#         super().__init__(window)

window = customtkinter.CTk()
window.title('Animate')
window.geometry('600x450')


def move_button():
    global button_x
    button_x += 0.001
    print(button_x)
    button.place(relx=button_x, rely=0.05, anchor='center')
    

    if button_x < 0.9:
        window.after(10, move_button)




    # colors = ['red', 'blue', 'yellow', 'pink', 'green', 'teal', 'white']
    # color = choice(colors)
    # button.configure(fg_color=color)

        
# def infinite_print():
#     print('infinite')
#     window.after(1000, infinite_print)


def infinite_print():
    global button_x
    button_x += 0.5
    if button_x < 10:
        print('infinite')
        print(button_x)
        window.after(1000, infinite_print)


button_x = 0.5

button = customtkinter.CTkButton(window, text='Slide me', command=move_button)
# button = customtkinter.CTkButton(window, text='Slide me', command=infinite_print)
button.place(relx=button_x, rely=0.5, anchor='center')


window.mainloop()



class SlidePannel(customtkinter.CTkFrame):
    def __init__(self, parent, start_pos, end_pos):
        super().__init__(master = parent, fg_color='#173540')
        
        """general attributes"""
        self.start_pos = start_pos + 0.04
        self.end_pos = end_pos - 0.03
        self.width = abs(start_pos - end_pos)

        """animation logic"""
        self.pos = self.start_pos
        self.in_start_pos = True

        """layout"""
        # self.place(relx=self.start_pos, rely=0, relwidth=self.width, relheight=1)
        self.place(relx=self.start_pos, rely=0.05, relwidth=self.width, relheight=0.9)

        
    
    def animate(self):
        if self.in_start_pos:
            self.animate_forward()
        else:
            self.animate_backwards()

    def animate_forward(self):
        if self.pos > self.end_pos:
            self.pos -= 0.008
            self.place(relx=self.pos, rely=0.05, relwidth=self.width, relheight=0.9)
            self.after(10, self.animate_forward)
        else:
            self.in_start_pos = False

    def animate_backwards(self):
        if self.pos < self.start_pos:
            self.pos += 0.008
            self.place(relx=self.pos, rely=0.05, relwidth=self.width, relheight=0.9)
            self.after(10, self.animate_backwards)
        else:
            self.in_start_pos = True




window = customtkinter.CTk()
window.geometry('600x450')


button_x = 0.5


# animated_panel = SlidePannel(window, 0.7, 1) ##position start from right
# animated_panel = SlidePannel(window, 0, -0.3) #position start from left
animated_panel = SlidePannel(window, 1.0, 0.7) #position start from zero *not showing


button = customtkinter.CTkButton(window, text='Slide me', command=animated_panel.animate)
button.place(relx=button_x, rely=0.5, anchor='center')


window.mainloop()