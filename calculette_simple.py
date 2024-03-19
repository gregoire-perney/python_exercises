nombre_a_gauche = input("Entrez le premier nombre: ")
operation = input("Entrez l'opérateur (+, -, *, /): ")
nombre_a_droite = input("Entrez le deuxième nombre: ")
resultat = 0
if (nombre_a_gauche.isnumeric() and nombre_a_droite.isnumeric()):
  nombre_a_gauche = int(nombre_a_gauche)
  nombre_a_droite = int(nombre_a_droite)
elif not nombre_a_gauche.isnumeric():
  print("Erreur: les deux nombres doivent être des nombres entiers")
  nombre_a_gauche = int(float(nombre_a_gauche))
  nombre_a_droite = int(nombre_a_droite)
  print(f"La valeur du nombre de gauche a été arrondie à un entier: {nombre_a_gauche}")
elif not nombre_a_droite.isnumeric():
  print("Erreur: les deux nombres doivent être des nombres entiers")
  nombre_a_droite = int(float(nombre_a_droite))
  nombre_a_gauche = int(nombre_a_gauche)
  print(f"La valeur du nombre de droite a été arrondie à un entier: {nombre_a_droite}")
elif not (nombre_a_gauche.isnumeric() and nombre_a_droite.isnumeric()):
  print("Erreur: les deux nombres doivent être des nombres entiers")
  nombre_a_gauche = int(float(nombre_a_gauche))
  nombre_a_droite = int(float(nombre_a_droite))
  print(f"Les valeurs ont été arrondie à des entiers: {nombre_a_gauche} et {nombre_a_droite}")
match operation:
  case "+":
    resultat = nombre_a_gauche + nombre_a_droite
  case "-":
    resultat = nombre_a_gauche - nombre_a_droite
  case "*":
    resultat = nombre_a_gauche * nombre_a_droite
  case "/":
    if nombre_a_droite ==0:
      print("Erreur: impossible de diviser par zéro.")
      exit()
    else:
      resultat = nombre_a_gauche / nombre_a_droite
  case _:
    print("Erreur: le symbole d'opération doit être '+', '-', '*' ou '/'")
    exit()
print("Résultat:", resultat)