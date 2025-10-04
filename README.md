# PRODIGY_CS_03
This project is a Python-based interactive password complexity checker with a graphical user interface built using Tkinter.
It helps users create strong and secure passwords by checking them against a set of complexity rules and providing instant feedback.

The tool displays password rules clearly before the user starts typing, ensuring they know the criteria required for a strong password. Users can type their password into the entry field, and upon clicking “Check Password,” the program evaluates the password and gives feedback in color-coded form. Green feedback means the password meets all requirements, while red feedback shows what criteria are missing.

Key Features:
Graphical User Interface using Tkinter for easy interaction.
Shows password complexity criteria before password entry.

Checks for:
Minimum length (8 characters).
At least one uppercase letter.
At least one lowercase letter.
At least one numeric digit.
At least one special character (!@#$%^&* etc.).
Color-coded feedback (green for strong passwords, red for missing criteria).
Option to toggle password visibility while typing.

How it works:
The tool uses Python’s re module to evaluate the password against complexity rules.
A feedback section updates after checking, listing missing criteria or confirming password strength.
A checkbox allows users to toggle password visibility, making it both secure and convenient.
