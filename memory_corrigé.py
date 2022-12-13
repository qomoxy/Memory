import random as r
import time as t

cartes = ['🍀', '🌷', '🍊', '🍎', '🍒', '🍟', '⚽️',
          '🎮', '🚀', '🚅', '🌌', '🐘', '🐶', '🐱', '🐤', '🌈', '👖', '👓']
carteCachee = '❓'


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
            reponse_3 = str(input("\n Connaissez-vous les règles du mémory ? \noui ou non : "))
            continuer = False

        elif reponse == "non":
            continuer = False
            reponse_2 = str(input("\n Es-tu sûr jeune entrepreneur ?! \noui ou non : "))

            if reponse_2 == "non":
                continuer = True

            elif reponse_2 == "oui":
                print("\n Tu fait quoi ici ?? \n\n")
                continuer = True

            else:
                answer()
                continuer = True

        else:
            answer()

    continuer = True

    while continuer:

        if reponse_3 == "non":
            print(
                "\n  Voici les règles du mémory : \n vous retournez deux cartes. Si les symboles/images sont identiques, vous gagnez la paire constituée et rejouer. Si les symboles/images sont différentes, vous les reposez faces cachées là où elles étaient. La partie est terminée lorsque toutes les cartes ont été assemblées par paires.\n")
            pseudo = input("\n Quelle est votre pseudonyme jeune entrepreneur : ")
            print("\n  Que voulez vous comme difficulté ", pseudo, " ?")
            difficulter = str(input("facile, normal ou difficile : "))

            if difficulter == "facile" or difficulter == "normal" or difficulter == "difficile":
                continuer = False
            else:
                answer()

        elif reponse_3 == "oui":
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

    return [difficulter, pseudo]

def palette_visuel(difficulter):
    '''Créer un tableau de difficultter voulue pour qu'ils soit afficher'''
    if difficulter == "facile":
        Arrays = [["❓"] * 4 for alt in range(3)]  # Il faut 6 paires

    elif difficulter == "normal":
        Arrays = [["❓"] * 5 for alt in range(4)]  # Il faut 10 paires

    else:
        Arrays = [["❓"] * 7 for alt in range(5)]  # Il faut 17 paires + 1 symbole
    return Arrays

def AfficherTableau(arrays):

    texteAffiche = '   '
    for i in range(len(arrays)):
        texteAffiche += str(i) + '  '
    print(texteAffiche)

    for i in range(len(arrays)):
        texteAffiche = ''
        for carte in tab[i]:
            texteAffiche += '|' + carte
        print(str(i) + texteAffiche + '|')

def paletteCacher(difficulter):
    """Créer notre palette de départ en fonction de la difficulter choisie"""

    nombresIconesUtiles = 0
    icones =['🍀', '🌷', '🍊', '🍎', '🍒', '🍟', '⚽️',
          '🎮', '🚀', '🚅', '🌌', '🐘', '🐶', '🐱', '🐤', '🌈', '👖', '👓']


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

def choixJoueur(difficulter):
    """Choix colonne de jeu en fonction de la difficulté"""
    continuer = True
    while continuer:
        choixColonne1 = int(input("\nChoisi une colone : "))  # afficher un pseudo ?
        choixLigne1 = int(input("Choisi une ligne : "))  # afficher un pseudo ?
        choixColonne2 = int(input("Choisi une colone : "))  # afficher un pseudo ?
        choixLigne2 = int(input("Choisi une ligne : "))  # afficher un pseudo ?

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

    return [choixColonne1, choixLigne1, choixColonne2, choixLigne2]

def caseChoisie(choixColonne1, choixLigne1, choixColonne2, choixLigne2, tabJoueur, tabComplet):
    """Affecte au jeux du joueur la case de la grille choisi, en fonction du tableau complet"""
    if tabJoueur[choixColonne1][choixLigne1] != "¤" or tabJoueur[choixColonne2][choixLigne2] != "¤":
        answer()
        caseChoisie(choixColonne1, choixLigne1, choixColonne2, choixLigne2, tabJoueur, tabComplet)
    tabJoueur[choixColonne1][choixLigne1] = tabComplet[choixColonne1][choixLigne1]
    tabJoueur[choixColonne2][choixLigne2] = tabComplet[choixColonne2][choixLigne2]
    return tabJoueur

def CartesPareilles(choix, tableauBase):
    return tableauBase[choix[0][0]][choix[0][1]] == tableauBase[choix[1][0]][choix[1][1]]

def ChangerTableauJoueur(choix, carte, tableauJoueur):
    tableauJoueur[choix[0][0]][choix[0][1]] = carte
    tableauJoueur[choix[1][0]][choix[1][1]] = carte
