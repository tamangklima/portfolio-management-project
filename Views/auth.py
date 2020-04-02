import tkinter as tk
from tkinter import ttk
from Core.DatabaseConnections import PRMS_Database


class LoginPage(tk.Toplevel):
    def __init__(self, parent):
        super().__init__()
        self.root = parent
        title_styles = {"font": ("Trebuchet MS Bold", 16),
                        "background": "#3F6BAA",
                        "foreground": "#E1FFFF",
                        "justify": "left"}

        text_styles = {"font": ("Verdana", 14),
                       "background": "#3F6BAA",
                       "foreground": "#E1FFFF"}

        main_frame = tk.Frame(self, bg="#708090", height=431, width=626)
        main_frame.pack(fill="both", expand="true")
        self.title("PRMSystem")
        self.geometry("626x431")  # Sets window size to 626w x 431h pixels
        self.resizable(0, 0)  # This prevents any resizing of the screen

        self.background_image = tk.PhotoImage(file=r"Views\login_background.png")
        background_label = tk.Label(main_frame, image=self.background_image)
        background_label.place(relwidth=1, relheight=1)

        frame_login = tk.Frame(main_frame, bg="#3F6BAA", relief="groove", bd=2)
        frame_login.place(rely=0.30, relx=0.17, height=130, width=400)

        label_title = tk.Label(frame_login, title_styles, text="PRMSystem Login Page")
        label_title.grid(row=0, column=1, columnspan=1)
        label_user = tk.Label(frame_login, text_styles, text="Username:")
        label_user.grid(row=1, column=0)
        label_pw = tk.Label(frame_login, text_styles, text="Password:")
        label_pw.grid(row=2, column=0)

        self.entry_user = ttk.Entry(frame_login, width=45, cursor="xterm")
        self.entry_user.grid(row=1, column=1)
        self.entry_pw = ttk.Entry(frame_login, width=45, cursor="xterm", show="*")
        self.entry_pw.grid(row=2, column=1)

        btn = ttk.Button(frame_login, text="Login", style="btns.TButton", command=lambda: self.getlogin())
        btn.place(rely=0.70, relx=0.50)

        signup_btn = ttk.Button(frame_login, style="btns.TButton", text="Register", command=lambda: self.get_signup())
        signup_btn.place(rely=0.70, relx=0.75)

        label_user = tk.Label(main_frame, font=("Arial Black", 8), background="#3F6BAA", text="Created by Ramon Williams")
        label_user.place(rely=0.9, relx=0.7)

        s = ttk.Style()
        s.configure("btns.TButton", font=("Arial", 10, "bold"), background="#74CAE3")

    def get_signup(self):
        RegistrationPage()

    def getlogin(self):
        user = self.entry_user.get()
        pw = self.entry_pw.get()
        with PRMS_Database() as db:
            validation = db.Validate_login(user, pw)

        if validation:
            tk.messagebox.showinfo("Login Successful", f"Welcome {user}")
            self.root.deiconify()
            self.destroy()
        else:
            tk.messagebox.showerror("Information", "The Username or Password you have entered are incorrect ")


class RegistrationPage(tk.Toplevel):
    def __init__(self):
        super().__init__()

        text_styles = {"font": ("Verdana", 10),
                       "background": "#3F6BAA",
                       "foreground": "#E1FFFF"}

        main_frame = tk.Frame(self, bg="#3F6BAA", height=150, width=250)
        # pack_propagate prevents the window resizing to match the widgets
        main_frame.pack_propagate(0)
        main_frame.pack(fill="both", expand="true")

        self.geometry("250x150")
        self.resizable(0, 0)
        self.title("Registration")
        label_user = tk.Label(main_frame, text_styles, text="New Username:")
        label_user.grid(row=1, column=0)
        self.entry_user = ttk.Entry(main_frame, width=20, cursor="xterm")
        self.entry_user.grid(row=1, column=1)

        label_pw = tk.Label(main_frame, text_styles, text="New Password:")
        label_pw.grid(row=2, column=0)
        self.entry_pw = ttk.Entry(main_frame, width=20, cursor="xterm", show="*")
        self.entry_pw.grid(row=2, column=1)

        label_code = tk.Label(main_frame, text_styles, text="Passcode:")
        label_code.grid(row=3, column=0)
        self.entry_code = tk.Entry(main_frame, width=6, cursor="xterm", show="*")
        self.entry_code.grid(row=3, column=1)

        btn = ttk.Button(main_frame, text="Create Account", command=lambda: self.signup())
        btn.grid(row=4, column=1)

    def signup(self):
        user = self.entry_user.get()
        pw = self.entry_pw.get()
        passcode = self.entry_code.get()

        if passcode == "2019" and len(pw) > 4:
            with PRMS_Database() as db:
                status = db.registration(user, pw)
            if isinstance(status, str):
                tk.messagebox.showerror("Information", "The Username you have entered already exists.")
            else:
                tk.messagebox.showinfo("Information", "Your account has now been created.")
                self.destroy()
        else:
            tk.messagebox.showerror("Information", "The Passcode you have entered is incorrect or\nyour password needs to be longer than 4 values.")