import random 

def liste(t, min, max):
    return [random.randint(min, max) for _ in range(t)]

tableau = liste(6, 1, 110)
print (tableau )