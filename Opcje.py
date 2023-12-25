from Logika import MenuW
poziomt = 0
def PoziomTrudności():
    global poziomt
    Meniu = MenuW("KidBot(Łatwy)","TopBot(Trudny)")
    if Meniu == "KidBot(Łatwy)":
        poziomt = 0
        return
    elif Meniu == "TopBot(Trudny)":
        poziomt = 1
        return
