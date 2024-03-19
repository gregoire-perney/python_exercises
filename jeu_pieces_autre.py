import random
    
def pieceEquilibre():
    if random.uniform(0,1) <= 0.5:
        return 'pile'
    else:
        return 'face'

def pieceJeuA():
    if random.uniform(0,1) <= 0.49:
        return 'pile'
    else:
        return 'face'
    
def pieceJeuB1():
    if random.uniform(0,1) <= 0.09:
        return 'pile'
    else:
        return 'face'
    
def pieceJeuB2():
    if random.random() <= 0.74:
        return 'pile'
    else:
        return 'face'

def jeuA(capital, nb_lances):
    for i in range(nb_lances):
        piece = pieceJeuA()
        if piece == 'pile':
            capital += 1  # on gagne 1 euro si on a pile
        else:
            capital -= 1  # on perd 1 euro sinon

    print("A: Après", nb_lances, "lancés, on a", capital, "€ de capital")

def jeuB(capital, nb_lances):
    for i in range(nb_lances):
        if capital % 3 == 0:  # on vérifie si le capital est un multiple de 3 ou non
            piece = pieceJeuB1()
        else:
            piece = pieceJeuB2()

        if piece == 'pile':
            capital += 1  # on gagne 1 euro si on a pile
        else:
            capital -= 1  # on perd 1 euro sinon

    print("B: Après", nb_lances, "lancés, on a", capital, "€ de capital")

def jeuC(capital, nb_lances):
    for i in range(nb_lances):
        piece_choix_jeu = pieceEquilibre()
        
        if piece_choix_jeu == 'pile':
            piece = pieceJeuA()   # on part sur le jeu A si la pièce équilibrée tombe sur pile
            if piece == 'pile':
                capital += 1  # on gagne 1 euro si on a pile
            else:
                capital -= 1  # on perd 1 euro sinon
                
        else:   # On part sur le jeu B si la pièce équilibrée tombe sur face
            if capital % 3 == 0:  # on vérifie si le capital est un multiple de 3 ou non
                piece = pieceJeuB1()
            else:
                piece = pieceJeuB2()

            if piece == 'pile':
                capital += 1  # on gagne 1 euro si on a pile
            else:
                capital -= 1  # on perd 1 euro sinon
            

    print("C: Après", nb_lances, "lancés, on a", capital, "€ de capital")

if __name__ == "__main__":

    capital = 1000
    nb_lances = 1000000

    jeuA(capital, nb_lances)
    jeuB(capital, nb_lances)
    jeuC(capital, nb_lances)

    

    