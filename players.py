from pyscript import display

players = [
    "Seth Ngo",
    "Eduardo Hizon",
    "Anakin Cruz",
    "Mic Ramos",
    "Vito Garcia",
    "Neriza Santos",
    "Juan Dela Cruz",
    "Maria Reyes",
    "Carlo Mendoza",
    "Alyssa Torres"
]

for player in players:
    display(f"<li>{player}</li>", target="player_list")
