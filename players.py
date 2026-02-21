from pyscript import display, document

def player_display(e):
    document.getElementById('players').innerHTML = ""

    players = [
        "Seth Ngo", "Vito De Guzman", "Ishan Shrestha",
        "Tax Rivera", "Tar Canete", "Enzo Villegas",
        "Koby Baylon", "LeBron James", "Bronny James",
        "Aura Briguela", "Bini Mikha", "Daniel Padilla",
        "Kath Bernardo", "Malupiton", "Jacob Cortez", "Pres. BBM"
    ]

    for player in players:
        display(f"• {player}", target="players")