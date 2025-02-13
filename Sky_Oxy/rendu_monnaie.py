INF = 999999999999

def rendu_monnaie_dyn(P, X, memo):
    if X == 0:
        return 0
    if X in memo:
        return memo[X]
    
    mini = INF
    for piece in P:
        if piece <= X:
            nb = 1 + rendu_monnaie_dyn(P, X - piece, memo)
            mini = min(mini, nb)
    
    memo[X] = mini
    return mini

# Liste des pièces disponibles
pieces = [2, 5, 10, 50, 100]
# Montant à rendre
somme = 171
# Dictionnaire pour la mémoïsation
memo = {}

# Calcul du nombre minimal de pièces
resultat = rendu_monnaie_dyn(pieces, somme, memo)
print(f"Nombre minimal de pièces pour rendre {somme} cts : {resultat}")
