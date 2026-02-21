from pyscript import display, document

def intrams_qualifications(e):
    document.getElementById("output").innerHTML = ""

    grade_input = document.getElementById("grade").value.strip()
    section = document.getElementById("section").value.strip()

    reg = document.querySelector('input[name="reg"]:checked')
    med = document.querySelector('input[name="med"]:checked')

    if grade_input == "" or section == "" or reg is None or med is None:
        display("Please complete all required fields.", target="output")
        return

    if reg.value == "no":
        display("Please register online first.", target="output")
        return

    if med.value == "not":
        display("Medical clearance is required.", target="output")
        return

    grade = int(grade_input)

    if grade < 7 or grade > 10:
        display("Only Grades 7 to 10 are eligible.", target="output")
        return

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