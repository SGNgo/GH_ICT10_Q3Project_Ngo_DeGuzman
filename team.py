from pyscript import display, document

def intrams_qualifications(e):
    document.getElementById("output").innerHTML = ""

    grade_input = document.getElementById("grade").value
    section = document.getElementById("section").value
    reg = document.querySelector('input[name="reg"]:checked')
    med = document.querySelector('input[name="med"]:checked')

    # FIELDS
    if grade_input == "" or section == "":
        display("Please complete all required fields.", target="output")
    elif reg.value == "no":
        display("Please register online to join the intramurals.", target="output")
    elif med.value == "not":
        display("Please secure a medical clearance.", target="output")
    else:
        
        grade = int(grade_input)

        if grade < 7 or grade > 10:
            display("Only Grades 7 to 10 are eligible.", target="output")
        else:
            # TEAMS
            teams = {
                7: {"Ruby":"Yellow Tigers","Sapphire":"Blue Bears","Emerald":"Red Bulldogs","Topaz":"Green Hornets"},
                8: {"Ruby":"Blue Bears","Sapphire":"Red Bulldogs","Emerald":"Green Hornets","Topaz":"Yellow Tigers"},
                9: {"Ruby":"Red Bulldogs","Sapphire":"Green Hornets","Emerald":"Yellow Tigers","Topaz":"Blue Bears"},
                10: {"Ruby":"Blue Tigers","Sapphire":"Green Hornets","Emerald":"Yellow Tigers","Topaz":"Red Bulldogs"}
            }

            if section in teams[grade]:
                display(f"🎉 Grade {grade} {section} is part of the {teams[grade][section]}!", target="output")
            else:
                display("Invalid section.", target="output")
