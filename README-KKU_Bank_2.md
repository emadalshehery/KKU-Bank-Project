# KKU Bank – Console Banking System

A console-based banking simulation for **King Khalid University (KKU)**. Users create an account, log in with credentials and a PIN, then make deposits and withdrawals.

## Features

### 1. Account creation (with input validation)
| Field          | Rule                                                        |
|----------------|-------------------------------------------------------------|
| ZIP code       | Digits only                                                 |
| University ID  | Digits only                                                 |
| Phone number   | Digits only                                                 |
| University email | Must start with `447` and end with `@kku.edu.sa`          |
| Username / Password | Free text                                              |
| PIN            | Entered twice; both entries must match                      |

After creating the account the user is asked *"Do you have an account? 1=Yes 0=No"*. Answering `0` restarts account creation; `1` proceeds to login.

### 2. Login
The user enters username, password, and PIN. The prompt repeats until the credentials are accepted.

### 3. Transactions
- **Deposit (option 2):** amount must be a whole number from 1 to 5000.
- **Withdrawal (option 1):** amount must be at least 1 and not exceed the current balance.
- The updated balance is displayed after every successful transaction. The starting balance is `0`.

Invalid input (letters, out-of-range numbers, etc.) is caught and the user is asked to try again.

## Concepts practiced
- `while` loops for input validation and menus
- `try / except ValueError` for safe integer conversion
- String methods: `.isdigit()`, `.startswith()`, `.endswith()`
- Conditional logic and f-strings

## How to run
```bash
python KKU_Bank_2.py
```

## Notes and possible improvements
- All data (account, balance) is stored in memory only and is lost when the program ends.
- The transaction menu loops indefinitely; there is no "Exit" option (use `Ctrl + C`).
- The login check uses `User != UN and Pass != PW or PINU != PIN`, so a correct PIN with a wrong username or password would still pass. It should require all three to match, e.g. `User != UN or Pass != PW or PINU != PIN`.
- Passwords and PINs are stored and compared as plain text, which is fine for a learning project but not for real systems.
- Only one account can exist at a time.
