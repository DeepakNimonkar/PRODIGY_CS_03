import re
import tkinter as tk
from tkinter import messagebox

def check_password(password):
    feedback = []

    if len(password) < 8:
        feedback.append("At least 8 characters")
    if not re.search(r"[A-Z]", password):
        feedback.append("At least one uppercase letter")
    if not re.search(r"[a-z]", password):
        feedback.append("At least one lowercase letter")
    if not re.search(r"[0-9]", password):
        feedback.append("At least one number")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        feedback.append("At least one special character (!@#$%^&* etc.)")

    return feedback


def on_check():
    password = entry.get()
    issues = check_password(password)

    if not password:
        messagebox.showwarning("Input Error", "Please enter a password")
        return

    if not issues:
        feedback_label.config(text=" Strong password!", fg="green")
        issues_text.set("")
    else:
        feedback_label.config(text="⚠ Password issues found:", fg="red")
        issues_text.set("\n".join(f"- {issue}" for issue in issues))


def toggle_password():
    if show_var.get():
        entry.config(show="")
    else:
        entry.config(show="*")



root = tk.Tk()
root.title("Password Complexity Checker")
root.geometry("400x400")
root.configure(bg="#f0f0f0")

tk.Label(root, text="Password Complexity Checker", font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=10)

criteria_text = """
Password must meet these criteria:
- At least 8 characters long
- At least one uppercase letter
- At least one lowercase letter
- At least one number
- At least one special character (!@#$%^&* etc.)
"""
tk.Label(root, text=criteria_text, justify="left", bg="#f0f0f0").pack(pady=5)

tk.Label(root, text="Enter your password:", bg="#f0f0f0").pack(pady=5)
entry = tk.Entry(root, show="*", width=30)
entry.pack(pady=5)


show_var = tk.BooleanVar()
show_checkbox = tk.Checkbutton(root, text="Show Password", variable=show_var, command=toggle_password, bg="#f0f0f0")
show_checkbox.pack()

tk.Button(root, text="Check Password", command=on_check, bg="#4CAF50",fg="white").pack(pady=10)

feedback_label = tk.Label(root, text="", font=("Arial", 12, "bold"), bg="#f0f0f0")
feedback_label.pack()

issues_text = tk.StringVar()
tk.Label(root, textvariable=issues_text, justify="left", bg="#f0f0f0", fg="red").pack()

root.mainloop()
