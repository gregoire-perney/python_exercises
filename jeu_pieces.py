import random

def A(wallet, nombre_parties):
    walletA = wallet
    for i in range(nombre_parties):
        n = random.random()
        if  n < 0.49:
            #pile
            walletA +=1
        else :
            #face
            walletA -=1
    return walletA

def B(wallet, nombre_parties):
    walletB = wallet
    for i in range(nombre_parties):
        n = random.random()
        if walletB%3 ==0:
            if  n < 0.09:
                #pile
                walletB +=1
            else :
                #face
                walletB -=1
        else:
            if  n < 0.74:
                #pile
                walletB +=1
            else :
                #face
                walletB -=1
    return walletB

def C(wallet, nombre_parties):
    walletC = wallet
    for i in range(nombre_parties):
        n = random.random()
        if  n < 0.5:
            #pile
            if  n < 0.49:
                #pile
                walletC +=1
            else :
                #face
                walletC -=1
        else :
            #face
            if walletC%3 ==0:
                if  n < 0.09:
                    #pile
                    walletC +=1
                else :
                    #face
                    walletC -=1
            else:
                if  n < 0.74:
                    #pile
                    walletC +=1
                else :
                    #face
                    walletC -=1
    return walletC


def main():
    resultatA = A(wallet, nombre_parties)
    if resultatA>1000:
        print("Jeu A gagnant, vous avez :",resultatA, "€")
    else:
        print("Jeu A perdant, vous avez :",resultatA, "€")

    resultatB = B(wallet, nombre_parties)
    if resultatB>1000:
        print("Jeu B gagnant, vous avez :",resultatB, "€")
    else:
        print("Jeu B perdant, vous avez :",resultatB, "€")

    resultatC = C(wallet, nombre_parties)
    if resultatC>1000:
        print("Jeu C gagnant, vous avez :",resultatC, "€")
    else:
        print("Jeu C perdant, vous avez :",resultatC, "€")





if __name__ == "__main__":
    wallet = 1000
    nombre_parties = 1000000 #int(input("Saisissez le nombre de parties: "))
    main()


