from tkinter import *
from tkinter import messagebox

accounts = {}

# Functions
def create_account():
    acc = entry_acc.get()
    name = entry_name.get()
    bal = entry_balance.get()

    if acc in accounts:
        messagebox.showerror("Error", "Account already exists!")
    else:
        accounts[acc] = {"name": name, "balance": float(bal)}
        messagebox.showinfo("Success", "Account Created!")
        clear_fields()

def deposit_money():
    acc = entry_acc.get()
    amt = entry_amount.get()

    if acc in accounts:
        accounts[acc]["balance"] += float(amt)
        messagebox.showinfo("Success", "Money Deposited!")
        clear_fields()
    else:
        messagebox.showerror("Error", "Account not found!")

def withdraw_money():
    acc = entry_acc.get()
    amt = entry_amount.get()

    if acc in accounts:
        if float(amt) <= accounts[acc]["balance"]:
            accounts[acc]["balance"] -= float(amt)
            messagebox.showinfo("Success", "Money Withdrawn!")
            clear_fields()
        else:
            messagebox.showerror("Error", "Insufficient Balance!")
    else:
        messagebox.showerror("Error", "Account not found!")

def check_balance():
    acc = entry_acc.get()

    if acc in accounts:
        name = accounts[acc]["name"]
        bal = accounts[acc]["balance"]
        messagebox.showinfo("Account Details", f"Name: {name}\nBalance: ₹{bal}")
    else:
        messagebox.showerror("Error", "Account not found!")

def clear_fields():
    entry_acc.delete(0, END)
    entry_name.delete(0, END)
    entry_balance.delete(0, END)
    entry_amount.delete(0, END)

# Main Window
root = Tk()
root.title("💰 Bank Management System")
root.geometry("450x450")
root.config(bg="#1e1e2f")

# Title
Label(root, text="Bank Management System", 
      font=("Arial", 16, "bold"), 
      bg="#1e1e2f", fg="white").pack(pady=10)

# Frame (Form)
frame = Frame(root, bg="#2c2c3e", padx=20, pady=20)
frame.pack(pady=10)

# Labels + Entry
Label(frame, text="Account No", bg="#2c2c3e", fg="white").grid(row=0, column=0, sticky="w")
entry_acc = Entry(frame, width=25)
entry_acc.grid(row=0, column=1, pady=5)

Label(frame, text="Name", bg="#2c2c3e", fg="white").grid(row=1, column=0, sticky="w")
entry_name = Entry(frame, width=25)
entry_name.grid(row=1, column=1, pady=5)

Label(frame, text="Initial Balance", bg="#2c2c3e", fg="white").grid(row=2, column=0, sticky="w")
entry_balance = Entry(frame, width=25)
entry_balance.grid(row=2, column=1, pady=5)

Label(frame, text="Amount", bg="#2c2c3e", fg="white").grid(row=3, column=0, sticky="w")
entry_amount = Entry(frame, width=25)
entry_amount.grid(row=3, column=1, pady=5)

# Buttons Frame
btn_frame = Frame(root, bg="#1e1e2f")
btn_frame.pack(pady=10)

Button(btn_frame, text="Create Account", width=18, bg="#4CAF50", fg="white", command=create_account).grid(row=0, column=0, pady=5)
Button(btn_frame, text="Deposit Money", width=18, bg="#2196F3", fg="white", command=deposit_money).grid(row=1, column=0, pady=5)
Button(btn_frame, text="Withdraw Money", width=18, bg="#f44336", fg="white", command=withdraw_money).grid(row=2, column=0, pady=5)
Button(btn_frame, text="Check Balance", width=18, bg="#ff9800", fg="white", command=check_balance).grid(row=3, column=0, pady=5)
Button(btn_frame, text="Clear Fields", width=18, bg="#9E9E9E", command=clear_fields).grid(row=4, column=0, pady=5)
Button(btn_frame, text="Exit", width=18, bg="black", fg="white", command=root.quit).grid(row=5, column=0, pady=5)

root.mainloop()