
# ATM Machine Simulation

I recently developed an ATM Machine Simulation as part of my Python Development internship at OctaNet service private limited. This project simulates the basic functionalities of an ATM, allowing users to perform various banking transactions such as checking account balances, withdrawing cash, and depositing funds.


## Features

- User Authentication: Secure login using user ID and PIN.
- Balance Inquiry: Display current account balance.
- Cash Withdrawal: Withdraw specified amounts of money, with error handling for insufficient funds.
- Cash Deposit: Deposit specified amounts into the account.
- PIN Change: Change the account PIN after verifying the old PIN.
- Transaction History: Track and display recent transactions.
- Exit: Option to exit the session safely.




## Technology

**Programming Language:**  Python

**Tools:** Visual Studio Code (IDE), GitHub (for version control)


## Code Documentation:

**Class ATM:**

    '__init__:' Initializes the ATM with a balance and a PIN.
    'check_pin:' Verifies the entered PIN against the stored PIN.
    'balance_inquiry:' Returns the current balance.
    'withdraw_cash:' Withdraws a specified amount from the balance if sufficient funds are available.
    'deposit_cash:' Deposits a specified amount into the account.
    'pin_change:' Changes the account PIN if the old PIN is correct.
    'get_transaction_history:' Returns the list of recorded transactions.
**Main Function:**

Provides a menu for the user to interact with the ATM.
Calls the appropriate method based on user input.
Continues running until the user chooses to exit.
