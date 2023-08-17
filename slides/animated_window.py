import customtkinter


class SlidePanel(customtkinter.CTkFrame):

    def __init__(self, parent, start_pos, end_pos):
        super().__init__(master=parent, corner_radius=5,
                         bg_color='transparent', height=600,
                         fg_color='#FFFFFF', width=100)

        # General attributes
        self.start_pos = start_pos + 0.04
        self.end_pos = end_pos - 0.04
        self.width = abs(start_pos - end_pos)

        # Animation logic
        self.pos = self.start_pos
        self.in_start_pos = True

        # Layout
        self.place(relx=self.start_pos, rely=0.05, relwidth=self.width, relheight=0.9)


    def animate(self) -> None:
        if self.in_start_pos:
            self.animate_forward()
        else:
            self.animate_backwards()

    def animate_forward(self) -> None:
        if self.pos > self.end_pos:
            self.pos -= 0.014
            self.place(relx=self.pos, y=6, relwidth=self.width, relheight=0.9)
            self.after(1, self.animate_forward)
        else:
            self.in_start_pos = False

    def animate_backwards(self) -> None:
        if self.pos < self.start_pos:
            self.pos += 0.014
            self.place(relx=self.pos, y=6, relwidth=self.width, relheight=0.9)
            self.after(1, self.animate_backwards)
        else:
            self.in_start_pos = True
