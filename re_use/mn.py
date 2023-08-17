import tkinter as tk
from threading import Timer

class MyApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("400x300")
        self.root.title("Login")

        self.username_label = tk.Label(self.root, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()

        self.password_label = tk.Label(self.root, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(self.root, text="Login", command=self.login)
        self.login_button.pack()

        self.admin_dashboard = None
        self.logout_timer = None

        self.root.mainloop()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Check username and password against some authentication mechanism
        # Replace the condition below with your authentication logic
        if username == "admin" and password == "password":
            self.show_admin_dashboard()
        else:
            print('hhh')

    def show_admin_dashboard(self):
        self.root.withdraw()  # Hide the login screen

        self.admin_dashboard = tk.Toplevel()
        self.admin_dashboard.geometry("400x300")
        self.admin_dashboard.title("Admin Dashboard")

        self.admin_label = tk.Label(self.admin_dashboard, text="Welcome to the Admin Dashboard!")
        self.admin_label.pack()

        self.start_logout_timer()

    def start_logout_timer(self):
        if self.logout_timer is not None:
            self.logout_timer.cancel()

        # Set the timeout duration (in seconds)
        timeout_duration = 120  # 2 minutes

        # Start the timer
        self.logout_timer = Timer(timeout_duration, self.logout)
        self.logout_timer.start()

        self.admin_dashboard.bind("<Key>", self.reset_timer)  # Bind key events to reset the timer
        self.admin_dashboard.bind("<Button>", self.reset_timer)  # Bind mouse events to reset the timer

    def reset_timer(self, event=None):
        self.start_logout_timer()

    def logout(self):
        if self.admin_dashboard:
            self.admin_dashboard.destroy()  # Close the admin dashboard window

        self.root.deiconify()  # Show the login screen
        self.logout_timer = None


if __name__ == "__main__":
    app = MyApp()
