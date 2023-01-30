from random import *  # pour mélanger le tableau


def memory():
    """
    Jeux du memory de luxe, c'est la fonction main du fichier. 
    Elle gère l'ensemble du jeu.
    Aucun return
    Aucuns paramètres d'entrée
    """

    s = start()  # démarrage du memory
    cmbJoueurs = s[0]
    difficulter = s[1]
    tabJoueur = paletteJoueur(difficulter)  # définie le tableau joueur
    tabCacher = paletteCacher(difficulter)  # définie le tableau caché, avec les résultats
    compteur = 0
    tabOrdiTmp = 1

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
            case = caseChoisie(colonne1, ligne1, colonne2, ligne2, tabJoueur, tabCacher)
            tabJoueur = case[0]
            affichage(tabJoueur)  # affiche ses choix au joueur
            input("Appuyez sur entrée si vous voulez passer : ")
            print("\n" * 50)
            p = paires(colonne1, ligne1, colonne2, ligne2, tabCacher, tabJoueur, allPaires,
                       case[1])  # vérifie s'il y a des paires
            tabJoueur = p[0]
            allPaires = p[1]
            continuer = win(allPaires, difficulter)  # affecte a continuer False si cest win
        affichage(tabCacher)
        print("\n Bravo ! T'as gagné ", pseudo, " en ", compteur, " tours." "\n")

    elif cmbJoueurs == "duo":

        pseudoJ1 = s[2]
        pseudoJ2 = s[3]

        allPairesJ1 = 0
        allPairesJ2 = 0

        continuer = True
        while continuer:  # continue tant qu'aucuns joueurs ne gagne
            compteur += 1
            print(pseudoJ1, " c'est à toi de jouer : ")
            affichage(tabJoueur)  # affiche le tableau avec les paires retournées s'il y en a
            choixJ1 = choixJoueur(difficulter)  # demande au joueur 1 ses choix pour retourner les cartes
            colonne1J1 = choixJ1[0]
            ligne1J1 = choixJ1[1]
            colonne2J1 = choixJ1[2]
            ligne2J1 = choixJ1[3]
            case = caseChoisie(colonne1J1, ligne1J1, colonne2J1, ligne2J1, tabJoueur, tabCacher)
            tabJoueur = case[0]
            affichage(tabJoueur)  # affiche ses choix au joueur 1
            input("Appuyez sur entrée, si vous voulez passer : ")
            print("\n" * 4)
            p1 = paires(colonne1J1, ligne1J1, colonne2J1, ligne2J1, tabCacher, tabJoueur, allPairesJ1, case[1])

            print(pseudoJ2, " c'est à toi de jouer : ")
            affichage(tabJoueur)  # affiche le tableau avec les paires retournées s'il y en a
            choixJ2 = choixJoueur(difficulter)  # demande au joueur 2 ses choix pour retourner les cartes
            colonne1J2 = choixJ2[0]
            ligne1J2 = choixJ2[1]
            colonne2J2 = choixJ2[2]
            ligne2J2 = choixJ2[3]
            case = caseChoisie(colonne1J2, ligne1J2, colonne2J2, ligne2J2, tabJoueur, tabCacher)
            tabJoueur = case[0]
            affichage(tabJoueur)  # affiche ses choix au joueur 2
            input("Appuyez sur entrée, si vous voulez passer : ")
            print("\n" * 4)
            p2 = paires(colonne1J2, ligne1J2, colonne2J2, ligne2J2, tabCacher, tabJoueur, allPairesJ2, case[1])

            tabJ1 = p1[0]
            tabJ2 = p2[0]

            allPairesJ1 = p1[1]
            allPairesJ2 = p2[1]

            tabJoueur = paireA2(tabJ1, tabJ2, tabJoueur)

            if win(allPairesJ1 + allPairesJ2, difficulter):
                continuer = True
            elif not win(allPairesJ1 + allPairesJ2, difficulter):
                continuer = False

        affichage(tabCacher)

        if allPairesJ1 == allPairesJ2:
            print("\n Bien joué à vous deux ! Vous êtes à égalité  ", pseudoJ1, "et", pseudoJ2, "\nVous avez fini en ",
                  compteur, " tours." "\n")
        elif allPairesJ2 > allPairesJ1:
            print("\n Bien joué ", pseudoJ2, " ! Tu as gagné avec  ", allPairesJ2, " points.", "Bien essayé ", pseudoJ1,
                  " ! Tu était à ", allPairesJ1, " points.", "\nVous avez fini en ", compteur, " tours." "\n")
        elif allPairesJ1 > allPairesJ2:
            print("\n Bien joué", pseudoJ1, " ! Tu as gagné avec  ", allPairesJ1, " points.", "Bien essayé ", pseudoJ2,
                  " ! Tu était à ", allPairesJ2, " points.", "\nVous avez fini en ", compteur, " tours." "\n")
        else:
            print("Fin de la game !")

    elif cmbJoueurs == "ordi":

        pseudo = s[2]

        allPaires = 0
        allPairesOrdi = 0

        continuer = True
        while continuer:  # continue tant que le joueur n'a pas gagné

            compteur += 1
            affichage(tabJoueur)  # affiche le tableau avec les paires retournées s'il y en a
            choix = choixJoueur(difficulter)  # demande au joueur ses choix pour retourner les cartes
            colonne1 = choix[0]
            ligne1 = choix[1]
            colonne2 = choix[2]
            ligne2 = choix[3]
            case = caseChoisie(colonne1, ligne1, colonne2, ligne2, tabJoueur, tabCacher)
            tabJoueur = case[0]
            affichage(tabJoueur)  # affiche ses choix au joueur
            input("Appuyez sur entrée si vous voulez passer : ")
            print("\n" * 4)
            p1 = paires(colonne1, ligne1, colonne2, ligne2, tabCacher, tabJoueur, allPaires, case[1])

            allPaires = p1[1]

            if win(allPaires + allPairesOrdi, difficulter):
                continuer = True
            elif not win(allPaires + allPairesOrdi, difficulter):
                continuer = False

            tabJoueur = p1[0]

            computer = ordi(difficulter, colonne1, ligne1, colonne2, ligne2, tabCacher, tabJoueur, tabOrdiTmp)
            case = caseChoisie(computer[0], computer[1], computer[2], computer[3], tabJoueur, tabCacher)
            tabJoueur = case[0]
            affichage(tabJoueur)

            tabOrdiTmp = computer[4]

            p2 = paires(computer[0], computer[1], computer[2], computer[3], tabCacher, tabJoueur, allPairesOrdi,case[1])  # vérifie s'il y a des paires

            tabJoueur = p2[0]

            allPairesOrdi = p2[1]

            if win(allPaires + allPairesOrdi, difficulter):
                continuer = True
            elif not win(allPaires + allPairesOrdi, difficulter):
                continuer = False

        affichage(tabCacher)

        if allPaires == allPairesOrdi:
            print("\n Bine joué à vous deux ! Vous êtes à égalité  ", pseudo, "et memory Bot", "\nVous avez fini en ",compteur, " tours." "\n")
        elif allPairesOrdi > allPaires:
            print("\n Une victoire de plus pour memory Bot  ! Il as gagné avec ", allPairesOrdi, " paires retournés.","Bien essayé ", pseudo, " ! Tu était à ", allPaires, " paires retournés.", "\nVous avez fini en ",compteur, " tours." "\n")
        elif allPaires > allPairesOrdi:
            print("\n Tu as triché", pseudo, " ! Tu as gagné avec  ", allPaires, " points.","Memory Bot reviendra  ! Il était à ", allPairesOrdi, " points.", "\nVous avez fini en ", compteur," tours." "\n")
        else:
            print("Fin de la game !")


def answer():  # à utiliser à chaque fois que le joueur ne répond pas correctement
    """
    Aucun paramètres d'entrés
    Affiche que la réponse effectuée est impossible
    return : ¡ Réponse pas executable ¡
    """
    print("\n ¡ Réponse pas executable ¡ \n")


def start():
    """
    Aucuns paramètres d'entrée
    Discours du debut avec règle et pseudo la difficulter et choix mode de jeu.
    return : choix du mode de jeu, difficulter et pseudo du ou des joueurs 
    """

    global reponseRegle
    continuer = True
    while continuer:
        reponseJeu = str(input(
            "\nBonjour à vous jeunes entrepreneurs, voulez vous jouer à ce magnifique jeu nommé 'memory' ? \noui ou non : "))

        if reponseJeu == "oui":
            reponseRegle = str(input("\n Connaissez-vous les règles du memory ? \noui ou non : "))
            if reponseRegle != "oui" and reponseRegle != "non":
                continuer = True
            else:
                continuer = False

        elif reponseJeu == "non":
            reponseSur = str(input("\n Êtes-vous sûrs jeunes entrepreneurs ?! \noui ou non : "))

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

    continuer = True
    while continuer:

        if reponseRegle == "non":
            print(
                "\n  Voici les règles du memory : \n Vous retournez deux cartes, si les symboles/images sont identiques, vous gagnez la paire constituée. Si les symboles/images sont différentes, vous les reposez faces cachées là où elles étaient. La partie est terminée lorsque toutes les cartes ont été assemblées par paires.\n ")

        elif reponseRegle != "oui":
            answer()
            continuer = True

        cmbJoueurs = str(input("\nVoulez-vous jouer en duo ou en solo ou contre un ordi : "))

        if cmbJoueurs == "solo":
            pseudo = input("\n Quelle est votre pseudonyme jeune entrepreneur : ")
            print("\n  Que voulez vous comme difficulté ", pseudo, " ?")
            difficulter = str(input("facile, normal ou difficile : "))
            if difficulter == "facile" or difficulter == "normal" or difficulter == "difficile":
                return ["solo", difficulter, pseudo]
            answer()
            continuer = True

        elif cmbJoueurs == "duo":
            print("\n\nQuels sont vos  pseudonymes jeunes entrepreneurs ? ")
            pseudoJ1 = input("\n Joueur 1 : ")
            pseudoJ2 = input("\n Joueur 2 : ")
            print("\n  Que voulez vous comme difficulté ", pseudoJ1, " et ", pseudoJ2, " ? ")
            difficulter = str(input("facile, normal ou difficile : "))
            if difficulter == "facile" or difficulter == "normal" or difficulter == "difficile":
                return ["duo", difficulter, pseudoJ1, pseudoJ2]
            answer()
            continuer = True

        if cmbJoueurs == "ordi":
            pseudo = input("\n Quelle est votre pseudonyme jeune entrepreneur : ")
            print("\n  Que voulez vous comme difficulté ", pseudo, " ? ")
            difficulter = str(input("facile, normal ou difficile : "))
            if difficulter == "facile" or difficulter == "normal" or difficulter == "difficile":
                return ["ordi", difficulter, pseudo]
            answer()
            continuer = True

        else:
            answer()


def paletteJoueur(difficulter):
    """
    Paramètres d'entrée : la difficulté du jeu
    Créer un tableau de difficulté voulue pour qu'il soit afficher
    return : un tableau a deux dimensions de la taille choisie par rapport à la difficulter et remplie.
    """

    if difficulter == "facile":
        arrays = [["⬜"] * 4 for _ in range(3)]  # Il faut 6 paires

    elif difficulter == "normal":
        arrays = [["⬜"] * 5 for _ in range(4)]  # Il faut 10 paires

    else:
        arrays = [["⬜"] * 7 for _ in range(5)]  # Il faut 17 paires + 1 symbole
    return arrays


def paletteCacher(difficulter):
    """
    Paramètre d'entrée : la difficulter du jeu
    Créer notre palette de départ en fonction de la difficulter choisie
    return : le tableau avec les réponses, avec le nombre de paires choisies et mélangés
    """

    icones = ['⚓', '⛳', '⛺', '⚽', '⛪', '⛅','⚖','✈','☘','⛵','⏰','☠','☢','✂','☎','⚙','⌨','✏','➰','❤']

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
    nombresIconesUtiles = (colonnes * lignes // 2) + (colonnes * lignes % 2)  # Calcul des icones utiles par rapport à la difficulté choisie
    trueArray = [None] * nombresIconesUtiles  # sert à créer la taille du tableau en 1 dimension

    for nb in range(nombresIconesUtiles):
        trueArray[nb] = icones[nb]

    trueArray += trueArray
    shuffle(trueArray)

    tabJoueur = [[None] * colonnes for _ in range(lignes)]  # sert à créer la taille du tableau en 2 dimensions
    for i in range(lignes):
        for j in range(colonnes):
            tabJoueur[i][j] = trueArray[colonnes * i + j]
    return tabJoueur


def affichage(arrays):
    """
    Paramètre d'entrée : un tableau a deux dimensions avec des caractères str à l'intérieur
    Sert à afficher le tableau joueur
    return : l'affichage du tableau
    """

    res = ""
    for i in range(len(arrays)):
        res += "\n"
        res += "|"
        for j in range(len(arrays[0])):
            res += arrays[i][j]
            res += "|"
    return print(res)


def verif(num_str):
    """
    Paramètre d'entrée : un str (un nombre de préférences)
    Sert à transformer les nombre str en int
    Si ce n'est pas possible, le nombre 1 est choisie
    return : le nombre en integer voulue
    """
    try:
        return int(num_str)
    except ValueError:
        answer()
        print("La première colonne/ligne a donc été choisie. ")
        return 1


def choixJoueur(difficulter):
    """
    Paramètre d'entrée : la difficulté du jeu
    Demande le choix colonne de jeu en fonction de la difficulté
    return : le choix de la premiere colonne du joueur, le choix de la premiere ligne du joueur, le choix de la seconde colonne du joueur, le choix de la seconde ligne du joueur
    """
    global choixColonne1, choixLigne1, choixColonne2, choixLigne2
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
            if 0 <= choixColonne1 <= 6 and 0 <= choixLigne1 <= 4 and 0 <= choixColonne2 <= 6 and 0 <= choixLigne2 <= 4:
                continuer = False
            else:
                answer()
                continuer = True

    return [choixColonne1, choixLigne1, choixColonne2, choixLigne2]


def caseChoisie(choixColonne1, choixLigne1, choixColonne2, choixLigne2, tabJoueur, tabComplet):
    """
    Paramètres d'entrée : le choix de la premiere colonne du joueur, le choix de la premiere ligne du joueur, le choix de la seconde colonne du joueur, le choix de la seconde ligne du joueur, le tableau joueur et le tableau remplis
    Affecte au jeu du joueur la case de la grille choisi (difficulté), en fonction du tableau complet
    return : le tableau du joueur avec les changements effectués et bool
    """

    Bool = -1  # Boolean : var int indice pour transmettre le choix de la fonction caseChoisie
    if tabJoueur[choixLigne1][choixColonne1] != "⬜" and tabJoueur[choixLigne2][choixColonne2] != "⬜":  # vérifie si c'est deja en paire
        print("\n\n\nT'as déjà découvert ces cartes, dommage tu perd un tour. ")
        Bool = 4
        return [tabJoueur, Bool]
    elif tabJoueur[choixLigne1][choixColonne1] != "⬜" or tabJoueur[choixLigne2][choixColonne2] != "⬜":
        print("\n\n\nT'as déjà découvert une de ces cartes, dommage tu perd un tour. ")
        Bool = 5
        return [tabJoueur, Bool]
    else:
        if tabJoueur[choixLigne1][choixColonne1] == tabComplet[choixLigne1][choixColonne1] and tabJoueur[choixLigne2][choixColonne2] == tabComplet[choixLigne2][choixColonne2]:
            Bool = 0
            return [tabJoueur, Bool]
        elif tabJoueur[choixLigne1][choixColonne1] == tabComplet[choixLigne1][choixColonne1]:
            tabJoueur[choixLigne2][choixColonne2] = tabComplet[choixLigne2][choixColonne2]
            Bool = 1
            return [tabJoueur, Bool]
        elif tabJoueur[choixLigne2][choixColonne2] == tabComplet[choixLigne2][choixColonne2]:
            tabJoueur[choixLigne1][choixColonne1] = tabComplet[choixLigne1][choixColonne1]
            Bool = 2
            return [tabJoueur, Bool]
        else:
            tabJoueur[choixLigne1][choixColonne1] = tabComplet[choixLigne1][choixColonne1]
            tabJoueur[choixLigne2][choixColonne2] = tabComplet[choixLigne2][choixColonne2]

            Bool = 3
            return [tabJoueur, Bool]  # renvoie un tableau avec les choix du joueur


def paires(choixColonne1, choixLigne1, choixColonne2, choixLigne2, tabComplet, tabJoueur, allPaires, Bool):
    """
    Paramètre d'entrée : le choix de la premiere colonne du joueur, le choix de la premiere ligne du joueur, le choix de la seconde colonne du joueur, le choix de la seconde ligne du joueur, le tableau remplis, le tableau joueur, le nombre de paires deja découvertes et bool
    Permet de determiner si les case choisies par le joueur sont paires
    En prenant en compte la difficulté
    return : le tableau du joueur avec les changements effectués et le nombre de paires deja effectués
    """
    paires = allPaires  # compteur de paire
    if Bool == 0:
        return [tabJoueur, paires]
    elif Bool == 1:
        tabJoueur[choixLigne2][choixColonne2] = "⬜"
        return [tabJoueur, paires]
    elif Bool == 2:
        tabJoueur[choixLigne1][choixColonne1] = tabComplet[choixLigne1][choixColonne1]
        return [tabJoueur, paires]
    elif Bool == 4:
        return [tabJoueur, paires]
    elif Bool == 5:
        return [tabJoueur, paires]
    elif tabComplet[choixLigne1][choixColonne1] == tabComplet[choixLigne2][choixColonne2]:
        tabJoueur[choixLigne1][choixColonne1] = tabComplet[choixLigne1][choixColonne1]
        tabJoueur[choixLigne2][choixColonne2] = tabComplet[choixLigne2][choixColonne2]
        paires += 1  # s'il y a paire : +1 au compteur

    elif tabJoueur[choixLigne1][choixColonne1] == tabComplet[choixLigne1][choixColonne1]:
        if tabJoueur[choixLigne2][choixColonne2] == tabComplet[choixLigne2][choixColonne2]:
            tabJoueur[choixLigne1][choixColonne1] = "⬜"
        tabJoueur[choixLigne2][choixColonne2] = "⬜"

    elif tabJoueur[choixLigne2][choixColonne2] == tabComplet[choixLigne2][choixColonne2]:
        tabJoueur[choixLigne1][choixColonne1] = "⬜"
    else:
        tabJoueur[choixLigne1][choixColonne1] = "⬜"
        tabJoueur[choixLigne2][choixColonne2] = "⬜"

    return [tabJoueur, paires]


def win(paires, difficulter):
    """
    Paramètres d'entrée : nombre de paires déjà trouvées par le joueur et difficulté du jeu
    Cette fonction sert à définir si le joueur est gagnant en fonction de sa difficulté et grace a aux nombres de paires découvertes
    return : False si c'est gagné sinon True
    """
    global paireATrouver
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
    """
    Paramètres d'entrée : tableau du joueur 1, tableau du joueur 2 et tableau des 2 joueurs réunis de la partie précédente
    Sert à assembler les deux tableaux joueur
    return : tableau des 2 joueurs réunis
    """
    for t in range(len(tabJ1)):
        for j in range(len(tabJ1[0])):
            if tabJ1[t][j] != "⬜":
                tabJoueur[t][j] = tabJ1[t][j]
    for i in range(len(tabJ2)):
        for j in range(len(tabJ2[0])):
            if tabJ2[i][j] != "⬜":
                tabJoueur[i][j] = tabJ2[i][j]
    return tabJoueur


def ordi(difficulter, colonne1, ligne1, colonne2, ligne2, tabCacher, tabJoueur, tabOrdiTmp):
    """
    Paramètres d'entrée : difficulté de jeu, le choix de la premiere colonne du joueur, le choix de la premiere ligne du joueur, le choix de la seconde colonne du joueur, le choix de la seconde ligne du joueur, le tableau remplis, le tableau joueur et le tableau ordi
    Joue comme un joueur, mais il a une tres bonne memoire, il enregistre toutes les cartes quil a joué et toutes les cartes jouées par le joueur
    return :  les coordonnés (x, y) (colonnes, lignes) du premier choix de l'ordi, puis le deuxième choix (colonnes, lignes) et le tableau de l'ordi pour retenir les emojies. 
    """

    global colonneChoix1
    
    if difficulter == "facile":
        colonnes = 4
        lignes = 3

    elif difficulter == "normal":
        colonnes = 5
        lignes = 4

    else:
        colonnes = 7
        lignes = 5

    if tabOrdiTmp == 1:
        tabOrdiTmp: list[list[str]] = paletteJoueur(difficulter)

    tabOrdiTmp[ligne1][colonne1] = tabCacher[ligne1][colonne1]
    tabOrdiTmp[ligne2][colonne2] = tabCacher[ligne2][colonne2]

    for x in range(lignes):
        for y in range(colonnes):
            if tabOrdiTmp[x][y] != "⬜":
                for i in range(lignes):
                    for j in range(colonnes):
                        if tabOrdiTmp[x][y] == tabOrdiTmp[i][j]:
                            if i == x and j == y:
                                continue
                            elif tabJoueur[i][j] == tabJoueur[x][y] and tabJoueur[x][y] != "⬜" and tabJoueur[i][j] != "⬜":
                                continue
                            else:
                                print("\nChoix Ordinateur : ")
                                print("\nChoisi une colonne : " + str(y + 1))
                                print("Choisi une ligne : " + str(x + 1))
                                print("Choisi une autre colonne : " + str(i + 1))
                                print("Et une autre ligne : " + str(j + 1))
                                tabOrdiTmp[i][j] = tabCacher[i][j]
                                return [y, x, j, i, tabOrdiTmp]

    ligneChoix1 = -1
    continuer = True
    while continuer:
        ligneChoix1 += 1
        for colonneChoix1 in range(colonnes):
            if tabOrdiTmp[ligneChoix1][colonneChoix1] == "⬜":
                print("\nChoix Ordinateur : ")
                print("\nChoisi une colonne : " + str(colonneChoix1 + 1))
                print("Choisi une ligne : " + str(ligneChoix1 + 1))
                continuer = False
                break

    ligneChoix2 = -1
    continuer = True
    while continuer:
        ligneChoix2 += 1
        for colonneChoix2 in range(colonnes):
            if tabOrdiTmp[ligneChoix2][colonneChoix2] == "⬜":
                if ligneChoix2 != ligneChoix1 or colonneChoix2 != colonneChoix1:
                    print(tabOrdiTmp[ligneChoix2][colonneChoix2] == "⬜")
                    print("Choisi une autre colonne : " + str(colonneChoix2 + 1))
                    print("Et une autre ligne : " + str(ligneChoix2 + 1))
                    tabOrdiTmp[ligneChoix1][colonneChoix1] = tabCacher[ligneChoix1][colonneChoix1]
                    tabOrdiTmp[ligneChoix2][colonneChoix2] = tabCacher[ligneChoix2][colonneChoix2]
                    return [colonneChoix1, ligneChoix1, colonneChoix2, ligneChoix2, tabOrdiTmp]

memory()
