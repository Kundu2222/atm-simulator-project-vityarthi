#  ATM Simulator

A simple and interactive **ATM Simulator built using Python**.

This project demonstrates how basic banking operations can be implemented using Python data structures, functions, loops, conditional statements, and user input.

---

##  Project Overview

The ATM Simulator allows a user to log in using their ATM PIN and perform several common banking operations.

After successful authentication, the user can:

*  Check account balance
*  Withdraw cash
*  Deposit cash
*  Change ATM PIN
*  View mini statement
*  View account details
*  Exit the ATM

The program also maintains a transaction history using a Python list.

---

##  Features

###  1. PIN Verification

The ATM asks the user to enter their 4-digit PIN.

If the PIN is correct:

```text
 PIN VERIFIED SUCCESSFULLY!
```

The user gets access to the ATM menu.

If the PIN is incorrect:

```text
 INCORRECT PIN
 ACCESS DENIED
```

---

###  2. Check Balance

The user can check their current account balance at any time.

Example:

```text
Available Balance : ₹50000
```

---

###  3. Withdraw Cash

The user can enter the amount they want to withdraw.

The program checks:

* Whether the amount is positive.
* Whether sufficient balance is available.
* Whether the transaction can be completed.

Example:

```text
 TRANSACTION SUCCESSFUL
Please collect your cash.
Amount Withdrawn : ₹5000
Remaining Balance: ₹45000
```

---

### 💳 4. Deposit Cash

The user can deposit money into their account.

The balance is automatically updated.

Example:

```text
DEPOSIT SUCCESSFUL
Amount Deposited : ₹3000
New Balance      : ₹48000
```

---

###  5. Change PIN

The user can change their ATM PIN by entering the old PIN.

The new PIN must contain exactly four digits.

If the old PIN is incorrect, the program provides an OTP-based verification option.

> Note: The OTP in this educational simulation is fixed and should not be considered real banking security.

---

###  6. Mini Statement

The program maintains a list of transactions.

Only the five most recent transactions are displayed.

Example:

```text
Recent Transactions:
--------------------
1 . Account opened with balance ₹50,000
2 . Deposited: ₹5000
3 . Withdrawn: ₹2000

Current Balance : ₹53000
```

---

###  7. Account Details

The program displays:

* Account holder name
* Account number
* Account status
* Current balance

Example:

```text
Account Holder : Pathikrit Kundu
Account Number : XXXX XXXX 4589
Account Status : ACTIVE
Balance        : ₹50000
```

---

##  Python Concepts Demonstrated

This project covers several important Python concepts.

| Concept              | Usage                              |
| -------------------- | ---------------------------------- |
| Dictionary           | Stores account information         |
| List                 | Stores transaction history         |
| Functions            | Creates reusable display functions |
| `while` loop         | Keeps the ATM running              |
| `for` loop           | Displays transactions              |
| `if-elif-else`       | Handles different ATM operations   |
| `enumerate()`        | Numbers transactions               |
| List slicing         | Gets the last five transactions    |
| `input()`            | Takes user input                   |
| Type conversion      | Converts input into integers       |
| Arithmetic operators | Updates account balance            |
| Comparison operators | Validates conditions               |

---

##  Data Structure

### Account Dictionary

```python
account = {
    "name": "Pathikrit Kundu",
    "account_no": "XXXX XXXX 4589",
    "pin": 2909,
    "balance": 50000
}
```

The dictionary stores all major account information.

### Transaction List

```python
transactions = [
    "Account opened with balance ₹50,000"
]
```

New transactions are added using:

```python
transactions.append()
```

---

##  Program Flow

```text
START
  │
  ▼
Display Welcome Screen
  │
  ▼
Enter ATM PIN
  │
  ├── Incorrect ──► Access Denied ──► END
  │
  ▼
PIN Verified
  │
  ▼
Display ATM Menu
  │
  ├── 1 → Check Balance
  │
  ├── 2 → Withdraw Cash
  │
  ├── 3 → Deposit Cash
  │
  ├── 4 → Change PIN
  │
  ├── 5 → Mini Statement
  │
  ├── 6 → Account Details
  │
  └── 7 → Exit
             │
             ▼
            END
```

---

##  How to Run

### Step 1 — Install Python

Install Python 3.x on your computer.

### Step 2 — Save the Program

Save the Python program as:

```text
atm_simulator.py
```

### Step 3 — Run the Program

Open a terminal in the project folder and run:

```bash
python atm_simulator.py
```

---

##  Demo Credentials

For this educational version:

```text
ATM PIN : 2909
OTP     : 1234
Initial Balance : ₹50,000
```

These credentials are only for demonstration purposes.

---

##  Project Structure

```text
ATM-Simulator/
│
├── atm_simulator.py
│
└── README.md
```

---

##  Disclaimer

This project is an **educational ATM simulation** created for learning Python programming.

It does not connect to an actual bank, ATM network, payment gateway, or financial database.

The PIN and OTP are stored directly in the program and therefore this implementation should **not** be used for real banking or financial transactions.

---

##  Possible Future Improvements

The project can be upgraded further by adding:

*  Multiple user accounts
*  Account lock after multiple wrong PIN attempts
*  Random OTP generation
*  Mobile-number verification
*  Transaction timestamps
*  File/database storage
*  Multiple bank accounts
*  Transfer money between accounts
*  Transaction summary
*  GUI using Tkinter
*  SQLite database integration
*  Password/PIN hashing
*  Light/Dark ATM interface

---

##  Project Type

**Language:** Python
**Project:** ATM Simulator
**Level:** Beginner → Intermediate
**Purpose:** Python programming practice and academic project

---

###  Learning Outcome

Through this project, the programmer learns how to combine Python's **data structures, functions, loops, conditions, input handling, and basic validation** to create a complete interactive application.
