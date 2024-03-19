nombres = input("Saisissez vos nombres: ")
        #Ici
liste = nombres.split()

liste_nums = []
for a in liste:
	liste_nums.append(int(a))    #On peut int() directement avant l'input()!!
#Cette boucle for est équivalente à la liste de compréhension :[int (x) for x in liste]

somme = 0
for b in liste_nums:
	somme = somme + b
print("Somme des nombres : ", somme)

moyenne = somme / len(liste_nums)
print("Moyenne des nombres : ", moyenne)

nombres_superieurs_moyenne = []
for c in liste_nums:
	if c > moyenne:
		nombres_superieurs_moyenne.append(c)
print("Nombre de nombres supérieurs à la moyenne : ", len(nombres_superieurs_moyenne),nombres_superieurs_moyenne)

nombres_pairs = []
d = 0
while d < len(liste_nums) : 
	if liste_nums[d] % 2 == 0:
		nombres_pairs.append(liste_nums[d])
		d += 1
	else:
		d += 1
print("Nombre de nombres pairs: ", len(nombres_pairs),nombres_pairs)