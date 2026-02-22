from pyscript import display, document

def player_display(e):
    document.getElementById('players').innerHTML = ""

    players = [
        "ASEO, TESSA",
        "BATAC, ANAKIN",
        "CALANGLANG, NERIZA",
        "DE GUZMAN, VITO",
        "DEE, AARON",
        "DOLOR, HARVEY",
        "GALVEZ, SELENA",
        "GARCES, ADRIANNA",
        "GROSPE, JILLIAN",
        "HIZON, EDUARDO",
        "INTALAN, MARGO",
        "KO, ATASHA",
        "LAGMAN, ALIJAH",
        "LAW, MARCUS",
        "MACABAGO, SITTIE",
        "MARTINEZ, EUAN",
        "MEDINA, KELSEY",
        "MENDOZA, MICHAELA",
        "MERGAL, MANUEL",
        "NGO, SETH",
        "PADOJINOG, SOFIA",
        "RIVERA, BENIGNO",
        "SHRESTHA, ISHAN",
        "UY, JENNIFER",
        "YAO, FRANCESCA"
    ]

    for i in range(len(players)):
        display(f"{i+1}. {players[i]}", target="players")