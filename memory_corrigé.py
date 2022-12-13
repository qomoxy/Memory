from random import *
from time import *


def memory():
    '''Jeux du memory'''
    s = start()
    difficulter = s[0]
    pseudo = s[1]
    tabJoueur = paletteJoueur(difficulter)
    tabCacher = paletteCacher(difficulter)
    
    continuer = True
    while continuer :
        affichage(tabJoueur)
        choices = choixJoueur(difficulter)
        
        
    
    


def answer():
    """Affiche que la reponse effectuée est impossible"""
    print("\n ¡ Réponse Inaxetable ¡ \n")


def start():
    """Discours du debut avec règle et pseudo, reponse : [difficulter, pseudo]"""

    continuer = True

    while continuer:
        reponse = str(input(
            "\nBonjour à vous jeune entrepreneur, voulez vous jouer à ce magnifique jeu nommé 'memory' ? \noui ou non : "))

        if reponse == "oui":
            reponse3 = str(input("\n Connaissez-vous les règles du mémory ? \noui ou non : "))
            continuer = False

        elif reponse == "non":
            reponse2 = str(input("\n Es-tu sûr jeune entrepreneur ?! \noui ou non : "))
            continuer = False

            if reponse2 == "non":
                continuer = True

            elif reponse2 == "oui":
                print("\n Tu fait quoi ici ?? \n\n")
                continuer = True

            else:
                answer()
                continuer = True

        else:
            answer()

    continuer = True

    while continuer:

        if reponse3 == "non":
            print(
                "\n  Voici les règles du mémory : \n vous retournez deux cartes. Si les symboles/images sont identiques, vous gagnez la paire constituée et rejouer. Si les symboles/images sont différentes, vous les reposez faces cachées là où elles étaient. La partie est terminée lorsque toutes les cartes ont été assemblées par paires.\n")
            pseudo = input("\n Quelle est votre pseudonyme jeune entrepreneur : ")
            print("\n  Que voulez vous comme difficulté ", pseudo, " ?")
            difficulter = str(input("facile, normal ou difficile : "))

            if difficulter == "facile" or difficulter == "normal" or difficulter == "difficile":
                continuer = False
            else:
                answer()

        elif reponse3 == "oui":
            pseudo = input("\n Quelle est votre pseudonyme jeune entrepreneur : ")
            print("\n Que voulez vous comme difficulté ?", pseudo)
            difficulter = str(input("facile ou normal ou difficile : "))

            if difficulter == "facile" or difficulter == "normal" or difficulter == "difficile":
                continuer = False
            else:
                answer()

        else:
            answer()
            continuer = True

    return [difficulter,pseudo]


def paletteJoueur(difficulter):
    """Créer un tableau de difficultter voulue pour qu'ils soit afficher"""
    if difficulter == "facile":
        arrays = [["¤"] * 4 for alt in range(3)]  # Il faut 6 paires

    elif difficulter == "normal":
        arrays = [["¤"] * 5 for alt in range(4)]  # Il faut 10 paires

    else:
        arrays = [["¤"] * 7 for alt in range(5)]  # Il faut 17 paires + 1 symbole
    return arrays


def paletteCacher(difficulter):
    """Créer notre palette de départ en fonction de la difficulter choisie"""

    nombresIconesUtiles = 0
    icones = ['⛾', '⛳', '✈', '⛴', '⛺', '⛟', '⛏', '⛄', '⛩', '⛥', '⚽', '⛪', '✂', '➹', 'a', 'b', 'c', 'd', 'e']

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
    nombresIconesUtiles = (colonnes * lignes // 2) + (colonnes * lignes % 2)  # Calcul des icones utiles
    trueArray = ["tmp"] * nombresIconesUtiles

    for i in range(nombresIconesUtiles):
        trueArray[i] = icones[i]

    trueArray += trueArray
    shuffle(trueArray)

    tabJoueur = [["a"] * colonnes for i in range(lignes)]
    for i in range(lignes):
        for j in range(colonnes):
            tabJoueur[i][j] = trueArray[colonnes * i + j]
    return tabJoueur


def affichage(arrays):
    """Sert à afficher le tableau joueur"""
    res = ""
    for i in range(len(arrays)):
        res += "\n |"
        for j in range(len(arrays[0])):
            res += arrays[i][j]
            res += "|"
    return print(res)


def choixJoueur(difficulter):
    """Choix colonne de jeu en fonction de la difficulté"""
    continuer = True
    while continuer:
        choixColonne1 = int(input("\nChoisi une colone : "))
        choixLigne1 = int(input("Choisi une ligne : "))
        choixColonne2 = int(input("Choisi une colone : "))
        choixLigne2 = int(input("Choisi une ligne : "))

        if choixColonne1 == choixColonne2 and choixLigne1 == choixLigne2:
            answer()
            continuer = True

        elif difficulter == "facile":
            if choixColonne1 >= 1 and choixColonne1 <= 4 and choixLigne1 >= 1 and choixLigne1 <= 3 and choixColonne2 >= 1 and choixColonne2 <= 4 and choixLigne2 >= 1 and choixLigne2 <= 3:
                continuer = False
            else:
                answer()
                continuer = True
        elif difficulter == "normal":
            if choixColonne1 >= 1 and choixColonne1 <= 5 and choixLigne1 >= 1 and choixLigne1 <= 4 and choixColonne2 >= 1 and choixColonne2 <= 5 and choixLigne2 >= 1 and choixLigne2 <= 4:
                continuer = False
            else:
                answer()
                continuer = True
        elif difficulter == "difficile":
            if choixColonne1 >= 1 and choixColonne1 <= 6 and choixLigne1 >= 1 and choixLigne1 <= 5 and choixColonne2 >= 1 and choixColonne2 <= 6 and choixLigne2 >= 1 and choixLigne2 <= 5:
                continuer = False
            else:
                answer()
                continuer = True

    return [[choixColonne1, choixLigne1, choixColonne2, choixLigne2]]


def caseChoisie(choixColonne1, choixLigne1, choixColonne2, choixLigne2, tabJoueur, tabComplet):
    """Affecte au jeux du joueur la case de la grille choisi, en fonction du tableau complet"""
    if tabJoueur[choixColonne1][choixLigne1] != "¤" or tabJoueur[choixColonne2][choixLigne2] != "¤": #verifie si cest deja en paire
        answer()
        caseChoisie(choixColonne1, choixLigne1, choixColonne2, choixLigne2, tabJoueur, tabComplet)
    tabJoueur[choixColonne1][choixLigne1] = tabComplet[choixColonne1][choixLigne1] #affecte la case choisie
    tabJoueur[choixColonne2][choixLigne2] = tabComplet[choixColonne2][choixLigne2] #affecte la case choisie
    return tabJoueur


def paires(choixColone1, choixLigne1, choixColone2, choixLigne2, tabComplet, tabJoueur, difficulter, allPaires,):  # marche pas -> pour test : paires(1,1,2,2,[['⛾','⛳','✈','⛴'],['⛾','⛳','✈','⛴'],['⛩','⛥','⚽','⛪'],['⛩','⛥','⚽','⛪']],[['¤','¤','¤','¤'],['¤','¤','¤','¤'],['¤','¤','¤','¤'],['¤','¤','¤','¤']],"facile",0)
    """
    Permet de determiner si les case choisies par le joueur sont paires
    En prenant en compte la difficulté
    """   
    paires = AllPaires
    
    if difficulter == "facile":
        paireATrouver = 6
    elif difficulter == "normal":
        paireATrouver = 10
    elif difficulter == "difficile":
        paireATrouver = 17

    continuer = True
    while continuer:
        if tabComplet(choixColone1,choixLigne1) == tabComplet(choixColone2,choixLigne2) :
            tabJoueur(choixColone1,choixLigne1) = tabComplet(choixColone2,choixLigne2)
            tabJoueur(choixColone1,choixLigne1) = tabComplet(choixColone2,choixLigne2)
            paires += 1
        return [tabJoueur,paires]
