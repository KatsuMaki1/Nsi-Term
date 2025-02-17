def recherche(Texte, Motif):
    Ltext = len(Texte)
    Lmotif = len(Motif)
    
    tab_caractere = [-1] * 256
    for i in range(Lmotif):
        tab_caractere[ord(Motif[i])] = i
        
    decalage = 0
    resultat = []
    
    while decalage <= Ltext - Lmotif:
        j = Lmotif - 1  
        
        while j >= 0 and Motif[j] == Texte[decalage + j]:
            j -= 1
            
        if j < 0:  # motif trouvé
            resultat.append(decalage)  # sauvegarde de la position
            
            if decalage + Lmotif < Ltext:
                decalage += Lmotif - tab_caractere[ord(Texte[decalage + Lmotif])]
            else:
                decalage += 1
        else:  # motif non trouvé, on décale
            maxi = max(1, j - tab_caractere[ord(Texte[decalage + j])])
            decalage += maxi
            
    return resultat


fichier = open("mettre son adresse personnel \\ 20000 lieues sous les mers - Jules Verne.txt", "r")
contenu = fichier.read()
fichier.close()


Motif = "Poisson"
positions = recherche(contenu, Motif)
print("Le motif a été trouvé aux positions :", positions)
