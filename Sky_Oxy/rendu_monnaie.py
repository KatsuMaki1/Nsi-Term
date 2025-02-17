INF = 999999999999

def rendu_monnaie_dyn(P, X, memo):
    mini = INF
    if X == 0:
        return 0
    elif memo[X]> 0:
        return 
    else : 
        for i in range (len(P)):
            if P[i] <= X:
                nb = 1 + rendu_monnaie_dyn(P, X - P[i],)
                if nb<mini:
                    mini = nb
                    memo[X] = mini
    return mini

pieces = [2, 5, 10, 50, 100]
somme = 171
memo = {}

resultat = rendu_monnaie_dyn(pieces, somme, memo)
print(f"Nombre minimal de pièces pour rendre {somme} cts : {resultat}")
