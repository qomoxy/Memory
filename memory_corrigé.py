from random import *


##desole si ya des fautes il est tard

def memory():
    '''Jeux du memory'''
    tmp = start()
    difficulter = tmp[0]
    pseudo = tmp[1]
    tabJoueur = palette_visuel(difficulter)
    tabComplet = paletteAleatoire(difficulter)
    
    waitWin = True
    while waitWin :
        affichage(tabJoueur)
        tmp = choixJoueur(difficulter)
        choixColonne1 = tmp[0]
        choixLigne1 = tmp[1]
        choixColonne2 = tmp[2]
        choixLigne2 = tmp[3]
        tabTmp = caseChoisie(choixColonne1, choixLigne1, choixColonne2, choixColonne2)
        affichage(tabTmp)
        tmp = paires(choixColonne1,choixLigne1,choixColonne2,choixLigne2,tabComplet,tabJoueur,difficulter)
        if tmp[0] == "Gagné" :
            print("t'as win bb")
            waitWin = False
        tabJoueur = tmp[1]
    affichage(tabJoueur)
        
def answer():
    """Affiche que la reponse effectuée est impossible"""    
    print("\n ¡ Réponse Inaxetable ¡ \n")

def start() :
    """Discours du debut, reponse : [difficulter, pseudo]"""
    
    continuer = True
    
    while continuer:
        réponse = str(input("\nBonjour à vous jeune entrepreneur, voulez vous jouer à ce magnifique jeu nommé 'memory' ? \noui ou non : "))
        
        if réponse == "oui" :
            réponse_3 = str(input("\n Connaissez-vous les règles du mémory ? \noui ou non : "))
            continuer = False
        
        elif réponse == "non" :
            réponse_2 = str(input("\n Es-tu sûr jeune entrepreneur ?! \noui ou non : "))
            continuer = False
        
        
            if réponse_2 == "non" :
                continuer = True
                
            elif réponse_2 == "oui" :
                print ("\n bah bouge de là sale chien !! \n\n")
                continuer = True
                
            else :
                answer()
                continuer = True
               
        else :
            answer()
            
    continuer = True
    
    while continuer:
        
        if réponse_3 == "non" :
            print("\n  Voici les règles du mémory : \n vous retournez deux cartes. Si les symboles/images sont identiques, vous gagnez la paire constituée et rejouer. Si les symboles/images sont différentes, vous les reposez faces cachées là où elles étaient. La partie est terminée lorsque toutes les cartes ont été assemblées par paires.\n")
            pseudo = input("\n Quelle est votre pseudonyme jeune entrepreneur : ")
            print("\n  Que voulez vous comme difficulté ", pseudo," ?")
            difficulté = str(input("facile, normal ou difficile : "))
            
            if difficulté == "facile" or difficulté == "normal" or difficulté == "difficile":
                continuer = False
            else:
                answer()

        elif réponse_3 == "oui" :
            pseudo = input("\n Quelle est votre pseudonyme jeune entrepreneur : ")
            print("\n Que voulez vous comme difficulté ?", pseudo)
            difficulté = str(input("facile ou normal ou difficile : "))
            
            if difficulté == "facile" or difficulté == "normal" or difficulté == "difficil":
                continuer = False
            else:
                answer()
        
        else :
            answer()
            continuer = True
        
    return [difficulté, pseudo]

def palette_visuel(difficulter):
    '''Créer un tableau de difficultter voulue pour qu'ils soit afficher'''    
    if difficulter == "facile" :
        Arrays = [["¤"]*4 for alt in range(3)]  #Il faut 6 paires
    
    elif difficulter == "normal" :
        Arrays = [["¤"]*5 for alt in range(4)]  #Il faut 10 paires

    else :
        Arrays = [["¤"]*7 for alt in range(5)]  #Il faut 17 paires + 1 symbole    
    return Arrays

def paletteAleatoire(difficulter): 
    """Créer notre palette de départ en fonction de la difficulter choisie"""
    
    nombresIconesUtiles = 0
    icones = ['⛾','⛳','✈','⛴','⛺','⛟','⛏','⛄','⛩','⛥','⚽','⛪','✂','➹','a','b','c','d','e']
    
    
    if difficulter == "facile" :
        colonnes = 4
        lignes = 3
        
    elif difficulter == "normal" :
        colonnes = 5
        lignes = 4

    else :
        colonnes = 7
        lignes = 5
        
    
    shuffle(icones) # Les icons sont placés aléatoirement
    nombresIconesUtiles = (colonnes * lignes // 2) + (colonnes * lignes % 2) # Calcul des icons utiles
    trueArray = ["tmp"]*nombresIconesUtiles
    
    for i in range(nombresIconesUtiles) :
        trueArray[i] = icones[i]
    
    trueArray += trueArray
    shuffle(trueArray)
    
    ##transformer en tableau a 2 dimentions
    
    return trueArray


def affichage(Arrays):
    """Sert à afficher le tableau joueur"""    
    res = ""
    for i in range(len(Arrays)) :
        res += "\n |"
        for j in range(len(Arrays[0])):
            res += Arrays[i][j]
            res += "|"
    return print(res)


def choixJoueur(difficulter):
    """Choix colonne de jeu"""
    continuer = True 
    while continuer:
        choix_colone1 = int(input("Choisi une colone : "))
        choix_ligne1 = int(input("Choisi une ligne : "))
        choix_colone2 = int(input("Choisi une colone : "))
        choix_ligne2 = int(input("Choisi une ligne : "))
        
        if difficulter == "facile" :
            if choix_colone1 >= 1 and choix_colone1 <= 4 and choix_ligne1 >= 1 and choix_ligne1 <= 3 and choix_colone2 >= 1 and choix_colone2 <= 4 and choix_ligne2 >= 1 and choix_ligne2 <= 3 : 
                continuer = False
            else:
                answer()
        elif difficulter == "normal" :
            if choix_colone1 >= 1 and choix_colone1 <= 5 and choix_ligne1 >= 1 and choix_ligne1 <= 4 and choix_colone2 >= 1 and choix_colone2 <= 5 and choix_ligne2 >= 1 and choix_ligne2 <= 4 : 
                continuer = False
            else:
                answer()
        elif difficulter == "difficile" :
            if choix_colone1 >= 1 and choix_colone1 <= 6 and choix_ligne1 >= 1 and choix_ligne1 <= 5 and choix_colone2 >= 1 and choix_colone2 <= 6 and choix_ligne2 >= 1 and choix_ligne2 <= 5 : 
                continuer = False
            else:
                answer()
        elif choix_colone1 == choixcolone2 and choix_ligne1 == choix_ligne2 :
            answer()
                   
    return [choix_colone1,choix_ligne1,choix_colone2,choix_ligne2]

def caseChoisie(choixColonne1, choixLigne1, choixColonne2, choixLigne2, tabJoueur, tabComplet) :
    """Affecte au jeux du joueur la case de la grille choisi, en fonction du tableau complet"""
    tabJoueur[choixColonne1][choixLigne1] = tabComplet[choixColonne1][choixLigne1]
    tabJoueur[choixColonne2][choixLigne2] = tabComplet[choixColonne2][choixLigne2]
    return tabJoueur

def paires(choixColone1,choixLigne1,choixColone2,choixLigne2,tabComplet,tabJoueur,difficulter):
    allPaires = []
    if difficulter == "facile" :
        paireATrouver = 6
    elif difficulter == "normal" :
        paireATrouver = 10
    elif difficulter == "difficile" :
        paireATrouver = 17
    
    continuer = True
    while continuer :
        if tabComplet[choixColone1][choixLigne1] == tabComplet[choixColone2][choixLigne2] :
            allPaires += tabComplet[choixColone1][choixLigne1]
            Arrays [choixColone1][choixLigne1] = tabComplet[choixColone1][choixLigne1]#mettre a jour le tabJoueur pour y voir la paire
            if len(allPaires) == paireATrouver :           
                return ["Gagné", tabJoueur]
            return ["non", tabJoueur]
            continuer = False
            
def affichageInGame(Arrays,tabComplet,choixColone1,choixLigne1,choixColone2,choixLigne2):  #ca sert a quoi ?
    Arrays [choixColone1][choixLigne1] = tabComplet[choixColone1][choixLigne1] #C'est index out of range
    Arrays [choixColone2][choixLigne2] = tabComplet[choixColone2][choixLigne2] #tabComplet n'est pas en cologne 
    res = ""
    for i in range(len(Arrays)) : #il faut l'afficher avec les cartes retourner 
        res += "\n |"
        for j in range(len(Arrays[0])):
            res += Arrays[i][j]
            res += "|"
    return print(res)
    
    

