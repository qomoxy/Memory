from random import *

#liste_symbole = ['⛾','⛳','✈','⛴','⛺','⛟','⛏','⛄','⛩','⛥','⚽','⛪','✂','➹']

def memory():
    ''''''
    start()
    palette_visuel(difficulté)
    
def answer():
    """Affiche que la reponse effectué est impossible"""    
    print("\n ¡ Réponse Inaxetable ¡ \n")

def start() :
    """Discours du debut, reponse : [difficulter, pseudo]"""
    
    continuer = True
    
    while continuer:
        réponse = str(input("Bonjour à vous jeune entrepreneur, voulez vous joué à ce magnifique jeu nommé 'memory' ? \noui ou non : "))
        
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
               
        else :
            answer()
            
    continuer = True
    
    while continuer:
        
        if réponse_3 == "non" :
            print("\n  Voici les règles du mémory : \n Le premier joueur retourne deux cartes. Si les images sont identiques, il gagne la paire constituée et rejoue. Si les images sont différentes, il les repose faces cachées là où elles étaient et c'est au joueur suivant de jouer. La partie est terminée lorsque toutes les cartes ont été assemblées par paires.\n")
            pseudo = input("\n Quelle est votre pseudonyme jeune entrepreneur : ")
            print("\n  Que voulez vous comme difficulté ", pseudo," ?")
            difficulté = str(input("facile, normal ou difficile : "))
            
            if difficulté == "facile" or difficulté == "normal" or difficulté == "difficile":
                continuer = False
            else:
                answer()

        elif réponse_3 == "oui" :
            pseudo = input("\n Quelle est votre pseudonyme jeune entrepreneur : ")
            print("\n  Que voulez vous comme difficulté ?", pseudo)
            difficulté = str(input("facile ou normal ou difficile : "))
            
            if difficulté == "facile" or difficulté == "normal" or difficulté == "difficil":
                continuer = False
            else:
                answer()
    return [difficulté, pseudo]


def palette_visuel(difficulté):
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


def palette_signes(difficulté):   #Maintenant c'est aléatoire mais il faut l'adapter avec la difficulté
    '''  '''
    index = 0
    
    if difficulter == "facile" :
        true_arrays = [[0]*4 for elt in range(3)]
        list1 = [1,2,3,4,5,6]
        limite = 5
        list2 = [0]*(limite*2)
        nb_lignes = 4
        nb_colones = 3
        
    elif difficulter == "normal" :
        true_arrays = [[0]*5 for elt in range(4)]
        list1 = [1,2,3,4,5,6,7,8,9,10]
        limite = 10
        list2 = [0]*(limite*2)
        nb_lignes = 5
        nb_colones = 4
        
    else :
        true_arrays = [[0]*7 for elt in range(5)]
        list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
        limite = 18
        list2 = [0]*17+1
        nb_lignes = 7
        nb_colones = 5
        
    for alt in range(len(list2)):
        list2[alt] = list1[index]
        index += 1
        if index = limite-1 :
            index = 0
    shuffle(list2)
    index = 0
    for i in range(nb_lignes):
        for x in range(nb_colones):
            true_arrays [i][x] = list2[index]
            index += 1
            if index > limite-1:
               index = 0
    shuffle(true_arrays)
    return true_arrays

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
    while continuer: # trouver un moyen pour prendre en compte les str pour éviter de faire des erreurs 
        choix_colone = int(input("Choisi une colone : "))
        choix_ligne = int(input("Choisi une ligne : "))
        
        if difficulter == "facile" :
            if choix_colone >= 1 and choix_colone <= 4 and choix_ligne >= 1 and choix_ligne <= 3 : 
                continuer = False
            else:
                answer()
        elif difficulter == "normal" :
            if choix_colone >= 1 and choix_colone <= 5 and choix_ligne >= 1 and choix_ligne <= 4 : 
                continuer = False
            else:
                answer()
        else :
            if choix_colone >= 1 and choix_colone <= 6 and choix_ligne >= 1 and choix_ligne <= 5 : 
                continuer = False
            else:
                answer()
        
    return [choix_colone,choix_ligne]
