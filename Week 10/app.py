import tkinter as tk
from tkinter import messagebox

file_name = "users.txt"

# File write Sign Up function
def sign_up(username, password):
    with open(file_name, "a") as file:
        file.write(f"{username},{password}\n")


# File read Sign In function
def sign_in(username, password):
    try:
        with open(file_name, "r") as file:
            users = file.readlines()
        for user in users:
            u, p = user.strip().split(",")
            if u == username and p == password:
                return True
        return False
    except FileNotFoundError:
        return False


# Helper function to clear window
def clear_window():
    for widget in root.winfo_children():
        widget.destroy()


# Sign In Window
def sign_in_window():
    clear_window()
    tk.Label(root, text="Sign In").pack()
    username_entry = tk.Entry(root)
    username_entry.pack()
    password_entry = tk.Entry(root, show="*")
    password_entry.pack()
    def login():
        username = username_entry.get().strip()
        password = password_entry.get().strip()
        # empty field check
        if username == "" or password == "":
            messagebox.showwarning("Empty Field", "Please fill in both Username and Password")
            return
        # check credentials
        if sign_in(username, password):
            messagebox.showinfo("Success", "Login Successful")
            main_menu()
        else:
            messagebox.showerror("Error", "Invalid Credentials")
    tk.Button(root, text="Sign In", command=login).pack()
    tk.Button(root, text="Go to Sign Up", command=sign_up_window).pack()

# Sign Up Window
def sign_up_window():
    clear_window()
    tk.Label(root, text="Sign Up").pack()
    username_entry = tk.Entry(root)
    username_entry.pack()
    password_entry = tk.Entry(root, show="*")
    password_entry.pack()
    def register():
        username = username_entry.get().strip()
        password = password_entry.get().strip()
        # check empty fields
        if username == "" or password == "":
            messagebox.showwarning("Empty Field", "Please fill in both Username and Password")
            return
        # save data
        sign_up(username, password)
        messagebox.showinfo("Success", "Account Created Successfully")
        sign_in_window()
    tk.Button(root, text="Sign Up", command=register).pack()
    tk.Button(root, text="Go to Sign In", command=sign_in_window).pack()


# Main Menu Window
def main_menu():
    clear_window()
    tk.Label(root, text="Welcome to Main Menu").pack()
    tk.Button(root, text="Logout", command=sign_in_window).pack()


# root window
root = tk.Tk()
root.title("Application")
root.geometry("300x200")

sign_in_window()

root.mainloop()