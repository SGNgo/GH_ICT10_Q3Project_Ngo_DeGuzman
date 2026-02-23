from pyscript import display, document  # Import PyScript functions

def intrams_qualifications(e):  # Function triggered when CHECK ELIGIBILITY button is clicked
    
    document.getElementById("output").innerHTML = ""

    grade_input = document.getElementById("grade").value.strip()
    section = document.getElementById("section").value.strip()

    # Gets selected radio buttons
    reg = document.querySelector('input[name="reg"]:checked')
    med = document.querySelector('input[name="med"]:checked')

    # CHECK IF ALL FIELDS ARE FILLED
    if grade_input == "" or section == "" or reg is None or med is None:
        display("Please complete all required fields.", target="output")
        return  # Stop function execution

    # CHECK REGISTRATION STATUS 
    if reg.value == "no":
        display("Please register online first.", target="output")
        return  # Stop execution if not registered

    # CHECK MEDICAL CLEARANCE
    if med.value == "not":
        display("Medical clearance is required.", target="output")
        return  # Stop execution if not cleared

    # Convert grade from string to integer
    grade = int(grade_input)

    # CHECK GRADE ELIGIBILITY 
    if grade < 7 or grade > 10:
        display("Only Grades 7 to 10 are eligible.", target="output")
        return

    # TEAMS
    teams = {
        7: {"Ruby":"Yellow Tigers","Sapphire":"Blue Bears","Emerald":"Red Bulldogs","Topaz":"Green Hornets"},
        8: {"Ruby":"Blue Bears","Sapphire":"Red Bulldogs","Emerald":"Green Hornets","Topaz":"Yellow Tigers"},
        9: {"Ruby":"Red Bulldogs","Sapphire":"Green Hornets","Emerald":"Yellow Tigers","Topaz":"Blue Bears"},
        10: {"Ruby":"Blue Bears","Sapphire":"Green Hornets","Emerald":"Yellow Tigers","Topaz":"Red Bulldogs"}
    }

    # SECTION AND GRADE TEAM DETERMINATION
    if section in teams[grade]:
        display(f"🎉 Grade {grade} {section} is part of the {teams[grade][section]}!", target="output")
    else:
        display("Invalid section.", target="output")
        

