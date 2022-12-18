from random import *  # pour mélanger le tableau


def memory():
    """Jeux du memory"""

    allPaires = 0
    s = start()  # démarrage du memory
    difficulter = s[0]
    pseudo = s[1]
    tabJoueur = paletteJoueur(difficulter)  # définie le tableau joueur
    tabCacher = paletteCacher(difficulter)  # définie le tableau caché, avec les résultats
    compteur = 0

    continuer = True
    while continuer:  # continue tant que le joueur n'a pas gagné
        compteur += 1
        affichage(tabJoueur)  # affiche le tableau avec les paires retournées s'il y en a
        choix = choixJoueur(difficulter)  # demande au joueur ses choix pour retourner les cartes
        colonne1 = choix[0]
        ligne1 = choix[1]
        colonne2 = choix[2]
        ligne2 = choix[3]
        affichage(caseChoisie(colonne1, ligne1, colonne2, ligne2, tabJoueur, tabCacher))  # affiche ses choix au joueur
        input("Appuyez sur entrée si vous voulez passer :")
        print("\n" * 50)
        p = paires(colonne1, ligne1, colonne2, ligne2, tabCacher, tabJoueur, allPaires)  # vérifie s'il y a des paires
        tabJoueur = p[0]
        allPaires = p[1]
        continuer = win(allPaires, difficulter)  # affecte a continuer False si cest win

    print("t'as gagné ", pseudo, "\n", affichage(tabCacher), "\n en ", compteur, " tours.")


def answer():  # à utiliser à chaque fois que le joueur ne répond pas correctement
    """Affiche que la réponse effectuée est impossible"""
    print("\n ¡ Réponse pas executable ¡ \n")


def start():
    """Discours du debut avec règle et pseudo, réponse : [difficulter, pseudo]"""

    continuer = True

    while continuer:
        reponseJeu = str(input(
            "\nBonjour à vous jeunes entrepreneurs, voulez vous jouer à ce magnifique jeu nommé 'memory' ? \noui ou non : "))

        if reponseJeu == "oui":
            reponseRegle = str(input("\n Connaissez-vous les règles du memory ? \noui ou non : "))
            continuer = False

        elif reponseJeu == "non":
            reponseSur = str(input("\n Êtes-vous sûrs jeunes entrepreneurs ?! \noui ou non : "))
            continuer = False

            if reponseSur == "non":
                continuer = True

            elif reponseSur == "oui":
                print("\n Tu fait quoi ici ?? \n\n")
                continuer = True

            else:
                answer()
                continuer = True

        else:
            answer()

    continuer = True

    while continuer:

        if reponseRegle == "non":
            print(
                "\n  Voici les règles du memory : \n Vous retournez deux cartes, si les symboles/images sont identiques, vous gagnez la paire constituée et rejouer. Si les symboles/images sont différentes, vous les reposez faces cachées là où elles étaient. La partie est terminée lorsque toutes les cartes ont été assemblées par paires.\n")
            pseudo = input("\n Quelle est votre pseudonyme jeune entrepreneur : ")
            print("\n  Que voulez vous comme difficulté ", pseudo, " ?")
            difficulter = str(input("facile, normal ou difficile : "))

            if difficulter == "facile" or difficulter == "normal" or difficulter == "difficile":
                continuer = False
            else:
                answer()

        elif reponseRegle == "oui":
            pseudo = input("\n Quelle est votre pseudonyme jeune entrepreneur : ")
            print("\n", pseudo, "que voulez vous comme difficulté ?")
            difficulter = str(input("facile ou normal ou difficile : "))

            if difficulter == "facile" or difficulter == "normal" or difficulter == "difficile":
                continuer = False
            else:
                answer()

        else:
            answer()
            continuer = True

    return [difficulter, pseudo]


def paletteJoueur(difficulter):
    """Créer un tableau de difficulté voulue pour qu'il soit afficher"""
    if difficulter == "facile":
        arrays = [["⬜"] * 4 for _ in range(3)]  # Il faut 6 paires

    elif difficulter == "normal":
        arrays = [["⬜"] * 5 for _ in range(4)]  # Il faut 10 paires

    else:
        arrays = [["⬜"] * 7 for _ in range(5)]  # Il faut 17 paires + 1 symbole
    return arrays


def paletteCacher(difficulter):
    """Créer notre palette de départ en fonction de la difficulter choisie"""

    icones = ['⚓', '⛳', '✈', '⛴', '⛺', '⛟', '⛏', '☂', '⚡', '⛥', '⚽', '⛪', '✂', '➹', '☀', '⌛', '⛅', '♻', '✉']

    if difficulter == "facile":
        colonnes = 4
        lignes = 3

    elif difficulter == "normal":
        colonnes = 5
        lignes = 4

    else:
        colonnes = 7
        lignes = 5

    shuffle(icones)  # Les icones sont placés aléatoirement
    nombresIconesUtiles = (colonnes * lignes // 2) + (
                colonnes * lignes % 2)  # Calcul des icones utiles par rapport à la difficulté choisie
    trueArray = ["tmp"] * nombresIconesUtiles  # sert à créer la taille du tableau en 1 dimension

    for i in range(nombresIconesUtiles):
        trueArray[i] = icones[i]

    trueArray += trueArray
    shuffle(trueArray)

    tabJoueur = [["a"] * colonnes for _ in range(lignes)]  # sert à créer la taille du tableau en 2 dimensions
    for i in range(lignes):
        for j in range(colonnes):
            tabJoueur[i][j] = trueArray[colonnes * i + j]
    return tabJoueur


def affichage(arrays):
    """Sert à afficher le tableau joueur"""
    res = ""
    for i in range(len(arrays)):
        res += "\n"
        res += "|"
        for j in range(len(arrays[0])):
            res += arrays[i][j]
            res += "|"
    return print(res)


def verif(num_str):
    continuer = True
    try:
        return int(num_str)
    except ValueError:
        answer()
        print("la première colonne/ligne a donc été choisie")
        return continuer


def choixJoueur(difficulter):
    """Choix colonne de jeu en fonction de la difficulté"""
    continuer = True
    while continuer:
        choixColonne1 = verif(str(input("\nChoisi une colonne : "))) - 1
        choixLigne1 = verif(str(input("Choisi une ligne : "))) - 1
        choixColonne2 = verif(str(input("Choisi une autre colonne : "))) - 1
        choixLigne2 = verif(str(input("Et une autre ligne : "))) - 1

        if choixColonne1 == choixColonne2 and choixLigne1 == choixLigne2:  # si il choisi une seule case : il recommence
            answer()
            continuer = True

        elif difficulter == "facile":
            if 0 <= choixColonne1 <= 3 and 0 <= choixLigne1 <= 2 and 0 <= choixColonne2 <= 3 and 0 <= choixLigne2 <= 2:
                continuer = False
            else:
                answer()
                continuer = True
        elif difficulter == "normal":
            if 0 <= choixColonne1 <= 4 and 0 <= choixLigne1 <= 3 and 0 <= choixColonne2 <= 4 and 0 <= choixLigne2 <= 3:
                continuer = False
            else:
                answer()
                continuer = True
        elif difficulter == "difficile":
            if 0 <= choixColonne1 <= 5 and 0 <= choixLigne1 <= 4 and 0 <= choixColonne2 <= 5 and 0 <= choixLigne2 <= 4:
                continuer = False
            else:
                answer()
                continuer = True

    return [choixColonne1, choixLigne1, choixColonne2, choixLigne2]


def caseChoisie(choixColonne1, choixLigne1, choixColonne2, choixLigne2, tabJoueur, tabComplet):
    """Affecte au jeu du joueur la case de la grille choisi, en fonction du tableau complet"""
    if tabJoueur[choixLigne2][choixColonne2] != "⬜":  # vérifie si c'est deja en paire
        print("\n\n\nT'as deja découvert cette carte, dommage tu perd un tour")
        if tabJoueur[choixLigne1][choixColonne1] != "⬜":
            print("\n\n\nT'as deja découvert cette carte, dommage tu perd un tour")
        else :
            tabJoueur[choixLigne1][choixColonne1] = tabComplet[choixLigne1][choixColonne1]
    elif tabJoueur[choixLigne1][choixColonne1] != "⬜":  # vérifie si c'est deja en paire
        print("\n\n\nT'as deja découvert cette carte, dommage tu perd un tour")
        if tabJoueur[choixLigne2][choixColonne2] != "⬜":
            print("\n\n\nT'as deja découvert cette carte, dommage tu perd un tour")
        else :
            tabJoueur[choixLigne2][choixColonne2] = tabComplet[choixLigne2][choixColonne2]
    else :
        tabJoueur[choixLigne1][choixColonne1] = tabComplet[choixLigne1][choixColonne1]  # affecte la case choisie
        tabJoueur[choixLigne2][choixColonne2] = tabComplet[choixLigne2][choixColonne2]  # affecte la case choisie
    return tabJoueur  # renvoie un tableau avec les choix du joueur


def paires(choixColonne1, choixLigne1, choixColonne2, choixLigne2, tabComplet, tabJoueur, allPaires):
    """
    Permet de determiner si les case choisies par le joueur sont paires
    En prenant en compte la difficulté
    """
    paires = allPaires  # compteur de paire
    if tabComplet[choixLigne1][choixColonne1] == tabComplet[choixLigne2][choixColonne2]:
        tabJoueur[choixLigne1][choixColonne1] = tabComplet[choixLigne1][choixColonne1]
        tabJoueur[choixLigne2][choixColonne2] = tabComplet[choixLigne2][choixColonne2]
        paires += 1  # s'il y a paire : +1 au compteur
    elif tabJoueur[choixLigne1][choixColonne1] == tabComplet[choixLigne1][choixColonne1]:
        tabJoueur[choixLigne2][choixColonne2] = "⬜"
    elif tabJoueur[choixLigne2][choixColonne2] == tabComplet[choixLigne2][choixColonne2]:
        tabJoueur[choixLigne1][choixColonne1] = "⬜"
    else:
        tabJoueur[choixLigne1][choixColonne1] = "⬜"
        tabJoueur[choixLigne2][choixColonne2] = "⬜"
    return [tabJoueur, paires]


def win(paires, difficulter):
    continuer = True
    while continuer:  # continue tant que le nombre de paires à trouver n'est pas trouvé
        if difficulter == "facile":
            paireATrouver = 6
            continuer = False
        elif difficulter == "normal":
            paireATrouver = 10
            continuer = False
        elif difficulter == "difficile":
            paireATrouver = 17
            continuer = False

    if paires == paireATrouver:  # vérifie si toutes les paires sont trouvées
        return False
    return True


memory()
