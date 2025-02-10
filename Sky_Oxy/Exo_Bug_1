from math import * 
import random
import time

def calcul(symbole, a, b):
    assert type(symbole) == str, 'Utiliser les bons chiffres'
    assert symbole == '+' or symbole == '-' or symbole == '*' or symbole == '/', 'Utiliser les bons  signes'
    if symbole == '/':
        assert b != 0, 'Ne pas utiliser 0 pour la division'
    
    if symbole == '+':
        resultat = a + b
    elif symbole == '-':
        resultat = a - b
    elif symbole == '*':
        resultat = a * b
    elif symbole == '/':
        resultat = a / b
    
    return resultat
print ('Calcul :',calcul('+',6,6))


def Division(a,b):
    """Calcul la division des deux nombres passés en paramètre

    Parameters:
        a : float, dividende de la division
        b : float, diviseur de la division

    Returns:
        Résultat de la division
    
    """
    return a/b

print ("Division :", Division(8,2))

def pythagore(a,b):
    c1= a**2 + b**2
    c2= sqrt (c1)
    return c2

print ("Pythagore : ", pythagore (3,4))

def NombreDeA(mot):
    return mot.count('a')

mot = "abracadabra"
print('Dans le mot ', mot , 'il y a', NombreDeA(mot), 'de "a"') 



#Division qui vérifie si b = à 0 ou pas ou autre erreur

a = 10
b = 2

try:
    c = a/b
    print("Le resultat est {}".format(c))
except ZeroDivisionError:
    print("Division par 0 impossible")
except TypeError:
    print("Erreur de type")
except:
    print("Une exception non gérée est survenue")


def division_euclidienne():
    try:
        a = int(input("Entrez le premier nombre (dividende) : "))
        b = int(input("Entrez le deuxième nombre (diviseur) : "))
        
        quotient, reste = divmod(a, b)
        print(f"Résultat : (Quotient: {quotient}, Reste: {reste})")
        return quotient, reste
    
    except ValueError:
        print("Erreur : Veuillez entrer des nombres entiers valides.")
    except ZeroDivisionError:
        print("Erreur : Division par zéro impossible.")
    except TypeError:
        print("Erreur : Entrée invalide. Assurez-vous d'entrer des nombres entiers.")
    except Exception as e:
        print(f"Une erreur inattendue s'est produite : {e}")

division_euclidienne()



def jeu_interruption():
    nombre_cible = random.randint(0, 1000)
    print(f"Essayez d'arrêter la boucle le plus proche de : {nombre_cible}")
    
    compteur = 0
    time.sleep(1.5)
    try:
        while True:
            print(f"Indice de boucle : {compteur}")
            compteur += 1
            if compteur == 1001: 
                print("Vous avez pas réussi à arrêter le compteur à temps !")
                break  # On sort de la boucle
            
            time.sleep(0.009)
            
    except KeyboardInterrupt:
        difference = abs(nombre_cible - compteur)
        
        print(f"\nVous avez arrêté à {compteur}. Différence : {difference}")
        print("Merci d'avoir joué !")

jeu_interruption()
