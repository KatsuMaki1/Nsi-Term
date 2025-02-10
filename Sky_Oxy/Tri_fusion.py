import random 

def liste(t, min, max):
    return [random.randint(min, max) for _ in range(t)]



def fusion(gauche, droite):
    resultat = []
    while gauche and droite:
        if gauche[0] < droite[0]:
            resultat.append(gauche.pop(0))
        else:
            resultat.append(droite.pop(0))
    resultat.extend(gauche if gauche else droite)
    return resultat

def tri_fusion(tableau):
    if len(tableau) <= 1:
        return "Le tableau n'a qu'une seul valeur", tableau
    milieu = len(tableau) // 2
    gauche = tri_fusion(tableau[:milieu])
    droite = tri_fusion(tableau[milieu:])
    return fusion(gauche, droite)


tableau = liste(1, 1, 100)
print("Tableau trié :", tri_fusion(tableau))
