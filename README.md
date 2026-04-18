# 💰 Bank Management System (GUI) - Documentation

## 1. Introduction
This project is a simple **Bank Management System** built using **Python and Tkinter**.  
It allows users to perform basic banking operations through a graphical interface.

---

## 2. Features
- Create Account
- Deposit Money
- Withdraw Money
- Check Balance
- User-friendly GUI

---

## 3. Data Structure Used
The program uses a **dictionary** to store account details.

### Example:
```python
accounts = {
    "101": {"name": "Rahul", "balance": 5000}
}
```

---

## 4. Functions Description

### 🔹 create_account()
Creates a new account with account number, name, and initial balance.

### 🔹 deposit_money()
Adds money to an existing account.

### 🔹 withdraw_money()
Withdraws money if sufficient balance is available.

### 🔹 check_balance()
Displays account holder name and current balance.

### 🔹 clear_fields()
Clears all input fields in GUI.

---

## 5. GUI Components
- Labels → Display text
- Entry → User input fields
- Buttons → Perform actions
- Messagebox → Show alerts/messages

---

## 6. Advantages
- Easy to use
- Beginner-friendly project
- Good for understanding GUI + dictionary

---

## 7. Limitations
- No data persistence (data lost after closing app)
- No login/authentication system
- Single user system

---

## 8. Conclusion
This project is a basic implementation of a banking system using Python GUI.  
It helps in understanding real-world logic and GUI development.

---

## 🚀 Future Improvements
- Add file saving (JSON/CSV)
- Add login system 🔐
- Convert to Web App (Flask/Django)
- Add table view for all accounts
