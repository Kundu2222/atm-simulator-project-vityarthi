# ==========================================================
#                    ATM SIMULATOR
# ==========================================================

# -------------------- ACCOUNT DATA ------------------------

account = {
    "name": "Pathikrit Kundu",
    "account_no": "XXXX XXXX 4589",
    "pin": 2909,
    "balance": 50000
}

# List to store all transactions
transactions = [
    "Account opened with balance ₹50,000"
]

# Fixed OTP for simulation
otp = 1234


# ==========================================================
#                    DISPLAY FUNCTIONS
# ==========================================================

def line():
    print("==================================================")


def welcome_screen():
    line()
    print("               WELCOME TO ATM ")
    line()
    print("              SECURE BANKING SYSTEM")
    line()


def show_menu():
    line()
    print("                    ATM MENU")
    line()
    print("   [1]  Check Balance")
    print("   [2]  Withdraw Cash")
    print("   [3]  Deposit Cash")
    print("   [4]  Change PIN")
    print("   [5]  Mini Statement")
    print("   [6]  Account Details")
    print("   [7]  Exit")
    line()


# ==========================================================
#                    PIN VERIFICATION
# ==========================================================

welcome_screen()

entered_pin = int(input(" Enter your 4-digit ATM PIN: "))

if entered_pin == account["pin"]:

    print("\nPIN VERIFIED SUCCESSFULLY!")
    print("Welcome,", account["name"])

    # ======================================================
    #                    MAIN ATM LOOP
    # ======================================================

    while True:

        show_menu()

        choice = int(input(" Enter your choice: "))

        # --------------------------------------------------
        # 1. CHECK BALANCE
        # --------------------------------------------------

        if choice == 1:

            line()
            print("                  BALANCE")
            line()

            print("Available Balance : ₹", account["balance"])

            line()


        # --------------------------------------------------
        # 2. WITHDRAW CASH
        # --------------------------------------------------

        elif choice == 2:

            line()
            print("                 WITHDRAW CASH")
            line()

            amount = int(input("Enter withdrawal amount: ₹"))

            if amount <= 0:

                print(" Invalid amount.")
                print("Please enter a positive amount.")

            elif amount > account["balance"]:

                print(" INSUFFICIENT BALANCE")
                print("Available balance: ₹", account["balance"])

            else:

                account["balance"] -= amount

                # Add transaction to list
                transactions.append(
                    "Withdrawn: ₹" + str(amount)
                )

                print("\n TRANSACTION SUCCESSFUL")
                print("Please collect your cash.")
                print("Amount Withdrawn : ₹", amount)
                print("Remaining Balance: ₹", account["balance"])


        # --------------------------------------------------
        # 3. DEPOSIT CASH
        # --------------------------------------------------

        elif choice == 3:

            line()
            print("                  DEPOSIT CASH")
            line()

            amount = int(input("Enter deposit amount: ₹"))

            if amount <= 0:

                print(" Invalid amount.")
                print("Please enter a positive amount.")

            else:

                account["balance"] += amount

                transactions.append(
                    "Deposited: ₹" + str(amount)
                )

                print("\n DEPOSIT SUCCESSFUL")
                print("Amount Deposited : ₹", amount)
                print("New Balance      : ₹", account["balance"])


        # --------------------------------------------------
        # 4. CHANGE PIN
        # --------------------------------------------------

        elif choice == 4:

            line()
            print("                   CHANGE PIN")
            line()

            old_pin = int(input("Enter your old PIN: "))

            if old_pin == account["pin"]:

                new_pin = int(
                    input("Enter your new 4-digit PIN: ")
                )

                if 1000 <= new_pin <= 9999:

                    account["pin"] = new_pin

                    transactions.append(
                        "ATM PIN changed successfully"
                    )

                    print("\n PIN CHANGED SUCCESSFULLY!")

                else:

                    print(" PIN must contain exactly 4 digits.")

            else:

                print(" Incorrect old PIN.")
                print("OTP verification required.")

                entered_otp = int(
                    input("Enter OTP: ")
                )

                if entered_otp == otp:

                    new_pin = int(
                        input("Enter your new 4-digit PIN: ")
                    )

                    if 1000 <= new_pin <= 9999:

                        account["pin"] = new_pin

                        transactions.append(
                            "ATM PIN changed using OTP"
                        )

                        print("\n PIN CHANGED SUCCESSFULLY!")

                    else:

                        print(" Invalid PIN.")

                else:

                    print(" Incorrect OTP.")
                    print("PIN change failed.")


        # --------------------------------------------------
        # 5. MINI STATEMENT
        # --------------------------------------------------

        elif choice == 5:

            line()
            print("                  MINI STATEMENT")
            line()

            print("Account Holder :", account["name"])
            print("Account Number :", account["account_no"])
            print()

            print("Recent Transactions:")
            print("--------------------")

            
            for number, transaction in enumerate(
                    transactions[-5:], start=1):

                print(number, ".", transaction)

            print()
            print("Current Balance : ₹", account["balance"])

            line()


        # --------------------------------------------------
        # 6. ACCOUNT DETAILS
        # --------------------------------------------------

        elif choice == 6:

            line()
            print("                  ACCOUNT DETAILS")
            line()

            print("Account Holder :", account["name"])
            print("Account Number :", account["account_no"])
            print("Account Status : ACTIVE")
            print("Balance        : ₹", account["balance"])

            line()


        # --------------------------------------------------
        # 7. EXIT
        # --------------------------------------------------

        elif choice == 7:

            line()
            print("             THANK YOU FOR USING")
            print("                  OUR ATM")
            line()

            print(" Account Holder :", account["name"])
            print(" Final Balance  : ₹", account["balance"])
            print()
            print("       Please take your card.")
            print("          Have a great day! ")

            line()

            break


        # --------------------------------------------------
        # INVALID CHOICE
        # --------------------------------------------------

        else:

            print("\n INVALID CHOICE")
            print("Please select a number from 1 to 7.")

# ==========================================================
#                    WRONG PIN
# ==========================================================

else:

    print("\n INCORRECT PIN")
    print(" ACCESS DENIED")
    print("Please collect your card.")