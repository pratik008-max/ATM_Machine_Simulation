class ATM:
    def __init__(self, balance=0, pin="1234"):
        """
        Initializes the ATM with a given balance and PIN.
        """
        self.balance = balance
        self.pin = pin
        self.transaction_history = []

    def check_pin(self, input_pin):
        """
        Verifies if the input PIN matches the stored PIN.

        Parameters:
        input_pin (str): The PIN entered by the user.

        Returns:
        bool: True if the PIN matches, False otherwise.
        """
        return self.pin == input_pin
    
    def balance_inquiry(self):
        """
        Returns the current account balance.

        Returns:
        float: The current balance.
        """
        return self.balance
    
    def withdraw_cash(self, withdrawal_amount):
        """
        Withdraws a specified amount from the balance.

        Parameters:
        withdrawal_amount (float): The amount to withdraw.

        Returns:
        str: A message indicating the result of the withdrawal.
        """
        if withdrawal_amount > 0:
            if self.balance >= withdrawal_amount:
                self.balance -= withdrawal_amount
                self.transaction_history.append(f"Withdrawal: ${withdrawal_amount}")
                return f"${withdrawal_amount} withdrawn successfully."
            else:
                return "Insufficient balance."
        else:
            return "Invalid withdrawal amount. Please enter a positive amount."
    
    def deposit_cash(self, amount):
        """
        Deposits a specified amount into the balance.

        Parameters:
        amount (float): The amount to deposit.

        Returns:
        str: A message indicating the result of the deposit.
        """
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposit: ${amount}")
            return f"${amount} deposited successfully."
        else:
            return "Invalid amount to deposit. Please check the amount."

    def pin_change(self, old_pin, new_pin):
        """
        Changes the account PIN if the old PIN is correct.

        Parameters:
        old_pin (str): The current PIN.
        new_pin (str): The new PIN to set.

        Returns:
        str: A message indicating the result of the PIN change.
        """
        if old_pin == self.pin:
            self.pin = new_pin
            self.transaction_history.append("PIN Change")
            return 'PIN changed successfully.'
        else:
            return "Invalid old PIN. Please try again."
    
    def get_transaction_history(self):
        """
        Returns the transaction history.

        Returns:
        list: A list of transaction records.
        """
        return self.transaction_history

def main():
    """
    Main function to interact with the ATM.
    """
    atm_1 = ATM(balance=20000, pin="2398")
    while True:
        print("\nWelcome to the Fastest ATM")
        print("""
                    1. Balance Inquiry
                    2. Withdraw Cash
                    3. Deposit Cash
                    4. Change PIN
                    5. Transaction History
                    6. Exit
            """)
        option = input("Enter any option from the above: ")

        if option == '1':
            print(f"Your current account balance is ${atm_1.balance_inquiry()}")
        elif option == '2':
            amount = float(input("Enter amount to withdraw: "))
            print(atm_1.withdraw_cash(amount))
        elif option == '3':
            amount = float(input("Enter amount to deposit: "))
            print(atm_1.deposit_cash(amount))
        elif option == '4':
            old_pin = input("Enter your old PIN: ")
            new_pin = input("Enter new PIN: ")
            print(atm_1.pin_change(old_pin, new_pin))
        elif option == '5':
            print("===== Transaction History =====")
            for transaction in atm_1.get_transaction_history():
                print(transaction)
        elif option == '6':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
