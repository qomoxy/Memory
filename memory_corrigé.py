from random import *

#liste_symbole = ['⛾','⛳','✈','⛴','⛺','⛟','⛏','⛄','⛩','⛥','⚽','⛪','✂','➹']

def memory():
    '''Jeux du memory'''
    start()
    palette_visuel(difficulté)
    
def answer():
    """Affiche que la reponse effectué est impossible"""    
    print("\n ¡ Réponse Inaxetable ¡ \n")

def start():
    """Discours du debut, reponse : [difficulter, pseudo]"""
    
    continuer = True
    
    while continuer:
        réponse = str(input("\nBonjour à vous jeune entrepreneur, voulez vous joué à ce magnifique jeu nommé 'memory' ? \noui ou non : "))
        
        if réponse == "oui" :
            réponse_3 = str(input("\n Connaissez-vous les règles du mémory ? \noui ou non : "))
            continuer = False
        
        elif réponse == "non" :
            réponse_2 = str(input("\n Est-tu sûr jeune entrepreneur ?! \noui ou non : "))
            continuer = False
        
        
            if réponse_2 == "non" :
                continuer = True
                
            elif réponse_2 == "oui" :
                print ("\n bah bouge de là sale chien !! \n\n")
                continuer = True  #si on trouve un autre moyen de recommencer sans bug ? Laisse le cette fois Quentin ou test tu verra que sans ça marche pas
               
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
    return [difficulté, pseudo]


def palette_visuel(difficulter):
    '''Créer un tableau de difficultter voulue pour qu'ils soit afficher'''
    difficulter = dif[0]
    
    if difficulter == "facile" :
        Arrays_f = [["¤"]*4 for alt in range(3)]  #Il faut 6 paires
        return Arrays_f
    
    elif difficulter == "normal" :
        Arrays_n = [["¤"]*5 for alt in range(4)]  #Il faut 10 paires
        return Arrays_n

    else :
        Arrays_d = [["¤"]*7 for alt in range(5)]  #Il faut 17 paires + 1 symbole
        return Arrays_d


def paletteAleatoire(difficulter):  #Equivalent palette_signes() mais qui fonctionne
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
    
    return trueArray


def affichage(palette_visuel):
    """Sert à afficher le tableau joueur"""
    res = ""
    for i in range(len(palette_visuel)) :
        res += "\n |"
        for j in range(len(palette_visuel[0])):
            res += palette_visuel[i][j]
            res += "|"
    return print(res)


def choix_joueur(difficulter):
    """Choix colonne de jeu"""
    continuer = True 
    while continuer: 
        choix_colone1 = int(input("Choisi une colone : "))
        choix_ligne1 = int(input("Choisi une ligne : "))
        
        if difficulter == "facile" :
            if choix_colone1 >= 1 and choix_colone1 <= 4 and choix_ligne1 >= 1 and choix_ligne1 <= 3 : 
                continuer = False
            else:
                answer()
        elif difficulter == "normal" :
            if choix_colone1 >= 1 and choix_colone1 <= 5 and choix_ligne1 >= 1 and choix_ligne1 <= 4 : 
                continuer = False
            else:
                answer()
        else :
            if choix_colone1 >= 1 and choix_colone1 <= 6 and choix_ligne1 >= 1 and choix_ligne1 <= 5 : 
                continuer = False
            else:
                answer()
        
    return [choix_colone1,choix_ligne1]


def caseChoisi(choixColonne, choixLigne) : #Afaire    
    return "tmp"

def paires(choix_colone1,choix_ligne1):  #Afaire
    return "tmp"
    


