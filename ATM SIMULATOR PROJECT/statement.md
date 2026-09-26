# ATM SIMULATOR — PROJECT STATEMENT

## Project Title

ATM Simulator using Python

## Problem Statement

The objective of this project is to develop a simple and interactive ATM Simulator using Python. The program simulates the basic operations performed by an ATM machine, allowing a user to securely access their bank account and perform different banking transactions.

The system first verifies the user's ATM PIN. After successful authentication, the user is provided with an ATM menu from which they can check their balance, withdraw money, deposit money, change their PIN, view a mini statement, and access account details.

The project uses Python concepts such as dictionaries, lists, functions, conditional statements, loops, user input, string manipulation, and the `enumerate()` function to create a structured and interactive banking application.

## Main Objectives

* Create a realistic ATM-like interface using Python.
* Store account information using a dictionary.
* Store transaction history using a list.
* Implement secure PIN verification.
* Allow cash withdrawal and deposit.
* Prevent withdrawal when the account has insufficient balance.
* Allow the user to change their ATM PIN.
* Provide OTP-based PIN-change verification.
* Display recent transactions through a mini statement.
* Display account information.
* Use loops to allow multiple operations during one session.
* Provide proper validation and error messages for invalid inputs.

## Features

1. **PIN Verification**

   * Verifies the user's 4-digit ATM PIN before granting access.

2. **Check Balance**

   * Displays the current available account balance.

3. **Withdraw Cash**

   * Allows the user to withdraw money.
   * Checks whether the entered amount is valid.
   * Prevents withdrawal when the balance is insufficient.

4. **Deposit Cash**

   * Allows the user to deposit money into the account.
   * Updates the account balance automatically.

5. **Change PIN**

   * Allows the user to change their existing PIN.
   * Uses OTP verification if the old PIN is entered incorrectly.

6. **Mini Statement**

   * Displays the five most recent transactions.
   * Shows the current account balance.

7. **Account Details**

   * Displays the account holder's name, account number, status, and balance.

8. **Exit**

   * Ends the ATM session and displays the final account balance.

## Python Concepts Used

* Variables
* Dictionaries
* Lists
* Functions
* `if`, `elif`, and `else`
* `while` loop
* `for` loop
* `enumerate()`
* User input using `input()`
* Type conversion using `int()`
* String concatenation
* List slicing
* Arithmetic operators
* Comparison operators
* Boolean conditions

## Expected Outcome

The final program should behave like a basic ATM system where a user can securely log in and perform different banking operations. All successful deposits, withdrawals, and PIN changes should be recorded in the transaction history, while the account balance should be updated after every financial transaction.

## Note

This project is an educational simulation only. It does not connect to a real bank account, banking server, or payment system.
