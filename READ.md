# Password Validation Program

## Description

This project is a simple Python program that checks whether a password meets basic security requirements. It gives clear messages when something is missing and asks the user to try again until a valid password is entered.

## Objective

To practice:
- Strings
- Conditions
- Loops
- Basic input validation

## Tools Used

- Python
- `string` module

## Validation Rules

The password must:

1. Be at least **8 characters long**
2. Contain at least one **uppercase letter**
3. Contain at least one **lowercase letter**
4. Contain at least one **number**
5. Contain at least one **special character**

## How It Works

1. The user enters a password.
2. The program checks each character.
3. It checks the password length.
4. If any requirement is missing, the program displays a clear message.
5. The user is asked to enter the password again.
6. The program stops when a valid password is entered.

## Example of Valid Password

```text
Hello@123
```

Output:

```text
Password is valid and strong!
```

## Example of Invalid Password

Input:

```text
hello123
```

Output:

```text
Uppercase letter is missing.
Special character is missing.
Please try again.
```

## Sample Program Output

```text
Enter your password: hello123

❌ Uppercase letter is missing.
❌ Special character is missing.
Please try again.

Enter your password: Hello123

❌ Special character is missing.
Please try again.

Enter your password: Hello@123

✅ Password is valid and strong!
```

## Key Concepts Practiced

- `input()` for user input
- `len()` for checking password length
- `for` loop for checking individual characters
- `while` loop for repeated validation
- `isupper()` for uppercase letters
- `islower()` for lowercase letters
- `isdigit()` for numbers
- `string.punctuation` for special characters
- `if` conditions for validation

## Security Note

The program does not print or display the password entered by the user. In real applications, passwords should not be stored or displayed as plain text.

## Conclusion

This project demonstrates basic password validation using Python strings, conditions, loops, and the `string` module.