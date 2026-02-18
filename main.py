from pyscript import display, document

def create_account(e):
    document.getElementById('output').innerHTML = ''
    username = document.getElementById('input1').value
    password = document.getElementById('input2').value

# USERNAME 
    if len(username) < 7:
        display('Username is too short. It must contain at least 7 characters.', target='output')

# PASSWORD 
    elif len(password) < 10:
        display('Password is too short. It must be at least 10 characters long.', target='output')
    elif password.isalpha():
        display('Password must contain at least one number.', target='output')
    elif password.isdigit():
        display('Password must contain at least one letter.', target='output')
    else:
        display('Account successfully created!', target='output')