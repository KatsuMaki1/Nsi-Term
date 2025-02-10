def fusion(gauche,droite):
    resultat = []
    while gauche and droite:
        if gauche[0] < droite[0]:
            resultat.append(gauche.pop(0))
        else:
            resultat.append(droite.pop(0))
    resultat.extend(gauche if gauche else droite)
    return resultat


def Tri_fusion(tableau):
    if len(tableau) <=1:
        return tableau
    couper = len(tableau) // 2
    gauche = Tri_fusion(tableau[:couper])
    droite = Tri_fusion(tableau[couper:])
    return fusion(gauche, droite)
    

tableau = [75, 37, 45, 110, 33, 97]
tableau_trie = Tri_fusion(tableau)
print("Tableau Trié:", tableau_trie)