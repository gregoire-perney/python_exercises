def salaire_mensuel(salaire_annuel):
	_salaire_mensuel = salaire_annuel / 12
	return _salaire_mensuel

def salaire_hebdomadaire(_salaire_mensuel):
	_salaire_hebdomadaire = _salaire_mensuel / 4
	return _salaire_hebdomadaire

def salaire_journalier(_salaire_hebdomadaire):
	_salaire_journalier = _salaire_hebdomadaire / 7
	return _salaire_journalier


def salaire_horaire(_salaire_hebdomadaire, heures_travaillees):
	_salaire_horaire = _salaire_hebdomadaire / heures_travaillees
	return _salaire_horaire

def main():
	salaire_annuel = int(input("Saisissez le salaire annuel : "))
	heures_travaillees = int(input("Saisissez le nombre d'heure travaillées par semaine : "))
	_salaire_mensuel = salaire_mensuel(salaire_annuel)
	_salaire_hebdomadaire = salaire_hebdomadaire(_salaire_mensuel)
	_salaire_journalier = salaire_journalier(_salaire_hebdomadaire)
	_salaire_horaire = salaire_horaire(_salaire_hebdomadaire, heures_travaillees)
	print(f"Votre salaire mensuel est de {_salaire_mensuel} euros")
	print(f"Votre salaire hebdomadaire est de {_salaire_hebdomadaire} euros")
	print(f"Votre salaire journalier est de {_salaire_journalier} euros")
	print(f"Votre salaire horaire est de {_salaire_horaire} euros")

main()
