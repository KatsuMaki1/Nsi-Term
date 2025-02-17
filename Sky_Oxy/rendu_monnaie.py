INF = 999999999999

def rendu_monnaie(P, X, memo):
    mini = INF
    if X == 0:
        return 0
    elif memo[X]> 0:
        return memo[X]
    else : 
        for i in range (len(P)):
            if P[i] <= X:
                nb = 1 + rendu_monnaie(P,X-P[i], memo)
                if nb<mini:
                    mini = nb
                    memo[X] = mini
    return mini

pieces = [2, 5, 10, 50, 100]
rendu = 171
m = [0] * (rendu + 1)
print (rendu_monnaie(pieces, rendu, m))
