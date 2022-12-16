from random import *  # pour mélanger le tableau

def memory():
    """Jeux du memory"""

    s = start()  # démarrage du memory
    cmbJoueurs = s[0]
    difficulter = s[1]
    tabJoueur = paletteJoueur(difficulter)  # définie le tableau joueur
    tabCacher = paletteCacher(difficulter)  # définie le tableau caché, avec les résultats
    compteur = 0

    if cmbJoueurs == "solo":

        pseudo = s[2]
        allPaires = 0

        continuer = True
        while continuer:  # continue tant que le joueur n'a pas gagné
            compteur += 1
            affichage(tabJoueur)  # affiche le tableau avec les paires retournées s'il y en a
            choix = choixJoueur(difficulter)  # demande au joueur ses choix pour retourner les cartes
            colonne1 = choix[0]
            ligne1 = choix[1]
            colonne2 = choix[2]
            ligne2 = choix[3]
            print("\n\nvisualisation 7s:")
            affichage(
                caseChoisie(colonne1, ligne1, colonne2, ligne2, tabJoueur, tabCacher))  # affiche ses choix au joueur
            sleep(7)  # patiente 7 secondes
            print("\n" * 50)
            p = paires(colonne1, ligne1, colonne2, ligne2, tabCacher, tabJoueur,
                       allPaires)  # vérifie s'il y a des paires
            tabJoueur = p[0]
            allPaires = p[1]
            continuer = win(allPaires, difficulter)  # affecte a continuer False si cest win

        print("t'as gagné ", pseudo, "\n", affichage(tabCacher), "\n en ", compteur, " tour.")

    elif cmbJoueurs == "duo":

        pseudoJ1 = s[2]
        pseudoJ2 = s[3]

        allPairesJ1 = 0
        allPairesJ2 = 0

        continuer = True
        while continuer:  # continue tant qu'aucuns joueurs ne gagne
            compteur += 1

            print(pseudoJ1, " c'est à toi de jouer :")
            affichage(tabJoueur)  # affiche le tableau avec les paires retournées s'il y en a
            choixJ1 = choixJoueur(difficulter)  # demande au joueur 1 ses choix pour retourner les cartes
            colonne1J1 = choixJ1[0]
            ligne1J1 = choixJ1[1]
            colonne2J1 = choixJ1[2]
            ligne2J1 = choixJ1[3]
            affichage(caseChoisie(colonne1J1, ligne1J1, colonne2J1, ligne2J1, tabJoueur,
                                  tabCacher))  # affiche ses choix au joueur 1
            passe = input("Appuyez sur entrée, si vous voulez passer : ")
            print("\n" * 4)

            print(pseudoJ2, " c'est à toi de jouer :")
            affichage(tabJoueur)  # affiche le tableau avec les paires retournées s'il y en a
            choixJ2 = choixJoueur(difficulter)  # demande au joueur 2 ses choix pour retourner les cartes
            colonne1J2 = choixJ2[0]
            ligne1J2 = choixJ2[1]
            colonne2J2 = choixJ2[2]
            ligne2J2 = choixJ2[3]
            affichage(caseChoisie(colonne1J2, ligne1J2, colonne2J2, ligne2J2, tabJoueur,
                                  tabCacher))  # affiche ses choix au joueur 2
            passe = input("Appuyez sur entrée, si vous voulez passer : ")
            print("\n" * 4)

            p1 = paires(colonne1J1, ligne1J1, colonne2J1, ligne2J1, tabCacher, tabJoueur, allPairesJ1)
            p2 = paires(colonne1J2, ligne1J2, colonne2J2, ligne2J2, tabCacher, tabJoueur, allPairesJ2)

            tabJ1 = p1[0]
            tabJ2 = p2[0]

            # Allpaire a faire

            tabJoueur = paireA2(tabJ1, tabJ2, tabJoueur)

            # win a faire


def answer():  # à utiliser à chaque fois que le joueur ne répond pas correctement
    """Affiche que la réponse effectuée est impossible"""
    print("\n ¡ Réponse pas executable ¡ \n")


def start():
    """Discours du debut avec règle et pseudo, réponse : la difficulter, le nombre de joueurs et leurs pseudos"""

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

        elif reponseRegle != "oui":
            answer()
            continuer = True

        cmbJoueurs = str(input("\nVoulez-vous jouer en duo ou en solo : "))

        if cmbJoueurs == "solo":
            pseudo = input("\n Quelle est votre pseudonyme jeune entrepreneur : ")
            print("\n  Que voulez vous comme difficulté ", pseudo, " ?")
            difficulter = str(input("facile, normal ou difficile : "))
            return ["solo", difficulter, pseudo]

        elif cmbJoueurs == "duo":
            print("\n\nQuels sont vos  pseudonymes jeunes entrepreneurs ?")
            pseudoJ1 = input("\n Joueur 1 : ")
            pseudoJ2 = input("\n Joueur 2 : ")
            print("\n  Que voulez vous comme difficulté ", pseudoJ1, " et ", pseudoJ2, " ?")
            difficulter = str(input("facile, normal ou difficile : "))
            return ["duo", difficulter, pseudoJ1, pseudoJ2]

        else:
            answer()


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

    nombresIconesUtiles = 0
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


def choixJoueur(difficulter):
    """Choix colonne de jeu en fonction de la difficulté"""
    continuer = True
    while continuer:
        choixColonne1 = int(input("\nChoisi une colonne : ")) - 1
        choixLigne1 = int(input("Choisi une ligne : ")) - 1
        choixColonne2 = int(input("Choisi une autre colonne : ")) - 1
        choixLigne2 = int(input("Et une autre ligne : ")) - 1

        if choixColonne1 == choixColonne2 and choixLigne1 == choixLigne2:  # si il choisi une seule case : il recommence
            answer()
            continuer = True

        elif difficulter == "facile":
            if 0 <= choixColonne1 <= 2 and 0 <= choixLigne1 <= 3 and 0 <= choixColonne2 <= 2 and 0 <= choixLigne2 <= 3:
                continuer = False
            else:
                answer()
                continuer = True
        elif difficulter == "normal":
            if 0 <= choixColonne1 <= 3 and 0 <= choixLigne1 <= 4 and 0 <= choixColonne2 <= 3 and 0 <= choixLigne2 <= 4:
                continuer = False
            else:
                answer()
                continuer = True
        elif difficulter == "difficile":
            if 0 <= choixColonne1 <= 4 and 0 <= choixLigne1 <= 5 and 0 <= choixColonne2 <= 4 and 0 <= choixLigne2 <= 5:
                continuer = False
            else:
                answer()
                continuer = True

    return [choixColonne1, choixLigne1, choixColonne2, choixLigne2]


def caseChoisie(choixColonne1, choixLigne1, choixColonne2, choixLigne2, tabJoueur, tabComplet):
    """Affecte au jeu du joueur la case de la grille choisi, en fonction du tableau complet"""
    if tabJoueur[choixColonne1][choixLigne1] != "⬜" or tabJoueur[choixColonne2][
        choixLigne2] != "⬜":  # vérifie si c'est deja en paire
        print("\n\n\nT'as deja découvert ces cartes, dommage tu perd un tour.")
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


def paireA2(tabJ1, tabJ2, tabJoueur):
    for i in range(len(tabJ1)):
        for j in range(len(tabJ1[0])):
            if tabJ1[i][j] != "⬜":
                tabJoueur[i][j] = tabJ1[i][j]
    for i in range(len(tabJ2)):
        for j in range(len(tabJ2[0])):
            if tabJ2[i][j] != "⬜":
                tabJoueur[i][j] = tabJ2[i][j]
    return tabJoueur


memory()
