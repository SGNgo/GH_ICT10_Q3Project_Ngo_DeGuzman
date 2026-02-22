from pyscript import display, document

def create_account(e):
    document.getElementById('output').innerHTML = ""

    username = document.getElementById('input1').value.strip()
    password = document.getElementById('input2').value.strip()

    # USERNAME CHECK
    if len(username) < 7:
        display("Username must contain at least 7 characters.", target="output")

    # PASSWORD CHECK
    elif len(password) < 10:
        display("Password must be at least 10 characters long.", target="output")
    # Password must contain at least one Number
    elif password.isalpha():
        display("Password must contain at least one number.", target="output")
    # Password must contain at least one Letter
    elif password.isdigit():
        display("Password must contain at least one letter.", target="output")
    # If all requirements are met, the account is successfully created
    else:

        display("✅ Account successfully created!", target="output")
